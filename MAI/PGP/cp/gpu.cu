#include "gpu.h"

//
// Kernel calculations 
//

__device__ uchar4 k_get_color(float value) {
    const int color_num = 15;
    const uchar4 color[color_num] = {
        make_uchar4(0, 0, 0, 95), 
        make_uchar4(0, 0, 120, 95), 
        make_uchar4(50, 50, 255, 95), 
        make_uchar4(0, 150, 255, 95), 
        make_uchar4(0, 255, 255, 135), 
        make_uchar4(0, 255, 150, 135), 
        make_uchar4(0, 255, 50, 135), 
        make_uchar4(50, 255, 50, 175), 
        make_uchar4(150, 255, 0, 175), 
        make_uchar4(255, 255, 0, 215), 
        make_uchar4(255, 155, 0, 215), 
        make_uchar4(255, 55, 0, 215), 
        make_uchar4(255, 0, 0, 255),
        make_uchar4(255, 120, 120, 255),
        make_uchar4(255, 255, 255, 255)
    };
 
    int id1, id2;
    float coef = 0;
    if (value <= 0) {  
        id1 = id2 = 0;            
    } else if (value >= 1) {  
        id1 = id2 = color_num - 1; 
    } else {
        value = value * (color_num - 1);     
        id1 = (int)value;                
        id2 = id1 + 1;                      
        coef = value - id1;  
    }  
    uchar4 c1 = color[id1], c2 = color[id2], res = color[id1];
    res.x += coef * (c2.x - c1.x);
    res.y += coef * (c2.y - c1.y);
    res.z += coef * (c2.z - c1.z);
    res.w += coef * (c2.w - c1.w);
    return res;
}

__global__ void k_draw_map(uchar4* data) {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    int idy = blockIdx.y * blockDim.y + threadIdx.y;
    int offsetx = blockDim.x * gridDim.x;
    int offsety = blockDim.y * gridDim.y;

    float x, y, f;
    for (int i = idx; i < WIDTH; i += offsetx) {
        x = k_point_S2Px(i);
        for (int j = idy; j < HEIGHT; j += offsety) {
            y = k_point_S2Py(j);
            f = F(x, y);
            float ratio = (f - K_F_MIN) / (K_F_MAX - K_F_MIN);
            data[j * WIDTH + i] = k_get_color(ratio);
        }
    }
}

__global__ void k_calc_fnc() {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    int idy = blockIdx.y * blockDim.y + threadIdx.y;
    int offsetx = blockDim.x * gridDim.x;
    int offsety = blockDim.y * gridDim.y;

    float x, y;
    for (int i = idx; i < WIDTH; i += offsetx) {
        x = k_point_S2Px(i);
        for (int j = idy; j < HEIGHT; j += offsety) {
            y = k_point_S2Py(j);
            fnc[j * WIDTH + i] = F(x, y);
        }
    }
}

void k_calc_minmax() {
    // calc min and max function value on screen, using thrust
    void *tmp;
    cudaMemcpyFromSymbol(&tmp, fnc, sizeof(float*));
    thrust::device_ptr<float> dev = thrust::device_pointer_cast((float*)tmp);
    thrust::pair<thrust::device_ptr<float>, thrust::device_ptr<float> > p = thrust::minmax_element(dev, dev + WIDTH * HEIGHT);
    F_MIN = p.first[0];
    F_MAX = p.second[0];
    KERNEL_PUSH(F_MIN, float);
    KERNEL_PUSH(F_MAX, float);
}

__global__ void k_draw_particle(uchar4* data) {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    int offsetx = blockDim.x * gridDim.x;
    float x, y;
    int xr, yr;
    float r = POINT_SIZE*POINT_SIZE;
    uchar4 tmp;
    for (int p = idx; p < P_NUM; p += offsetx) {
        x = points[p].x;
        y = points[p].y;
        if (x <= K_CENTER.x - K_RADIUS || 
            x >= K_CENTER.x + K_RADIUS ||
            y <= K_CENTER.y - K_RADIUS || 
            y >= K_CENTER.y + K_RADIUS)  continue;
        xr = max(0.0, k_point_P2Sx(x));
        yr = max(0.0, k_point_P2Sy(y));
        for (int i = xr-POINT_SIZE; i <= xr+POINT_SIZE; i++) {
            for (int j = yr-POINT_SIZE; j <= yr+POINT_SIZE; j++) {
                if (((i-xr)*(i-xr) + (j-yr)*(j-yr) <= r) && i>0 && j>0 && i<WIDTH && j<HEIGHT) {
                    tmp = data[j * WIDTH + i];
                    data[j * WIDTH + i] = make_uchar4(255-tmp.x, 255-tmp.y, 255-tmp.z, 255);
                }
            }
        }
    }
}

__global__ void k_calc_lbest() {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    int offsetx = blockDim.x * gridDim.x;
    float f;
    for (int i = idx; i < P_NUM; i += offsetx) {
        f = F(points[i].x, points[i].y);
        if (f < lbest[i].z) {
            lbest[i] = make_float3(points[i].x, points[i].y, f);
        }
    }
}

struct cmpr_lbest {
    __device__ bool operator()(float3 a, float3 b) {
        return a.z < b.z;
    }
};

void k_calc_gbest() {
    float3 *h_lbest;
    cudaMemcpyFromSymbol(&h_lbest, lbest, sizeof(float3*));
    thrust::device_ptr<float3> dev = thrust::device_pointer_cast(h_lbest);
    float3 extrm = thrust::min_element(dev, dev + P_NUM, cmpr_lbest())[0];

    float3 h_gbest;
    cudaMemcpyFromSymbol(&h_gbest, gbest, sizeof(float3));
    if (extrm.z < h_gbest.z) {
        CSC(cudaMemcpyToSymbol(gbest, &extrm, sizeof(float3)));
        printf("Global min = %f in (%f, %f)\n", extrm.z, extrm.x, extrm.y);
    }
}

__global__ void k_calc_particle(unsigned long long seed) {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    int offsetx = blockDim.x * gridDim.x;
    seed *= idx;
    curandState s;
    curand_init(seed, 0, 0, &s);

    float dt = K_PSO_DT;
    float a1 = PSO_A1 * dt, a2 = PSO_A2 * dt, w = PSO_W;
    float r1, r2;

    for (int p = idx; p < P_NUM; p += offsetx) {
        r1 = curand_uniform(&s);
        r2 = curand_uniform(&s);

        velocity[p].x = w * velocity[p].x +
            a1 * r1 * (lbest[p].x - points[p].x) +
            a2 * r2 * (gbest.x - points[p].x);

        r1 = curand_uniform(&s);
        r2 = curand_uniform(&s);

        velocity[p].y = w * velocity[p].y +
            a1 * r1 * (lbest[p].y - points[p].y) +
            a2 * r2 * (gbest.y - points[p].y);

        points[p].x += velocity[p].x * dt;
        points[p].y += velocity[p].y * dt;

        for (int i = 0; i < P_NUM; ++i){
            float2 p1 = points[p], p2 = points[i];
            if (i == p) continue;
            float r = (p1.x - p2.x)*(p1.x - p2.x) + (p1.y - p2.y)*(p1.y - p2.y);
            float2 v = make_float2(dt * (p1.x - p2.x) / (r * r), dt * (p1.y - p2.y) / (r * r));
            points[p].x += PSO_REP * v.x;
            points[p].y += PSO_REP * v.y;
        }
    }
}

__host__ __device__ float2 operator+(float2 a, float2 b) {
    return make_float2(a.x + b.x, a.y + b.y);
}

void k_calc_center() {
    void *h_points;
    cudaMemcpyFromSymbol(&h_points, points, sizeof(float2*));
    thrust::device_ptr<float2> dev = thrust::device_pointer_cast((float2*)h_points);
    float2 newCenter = thrust::reduce(dev, dev + P_NUM, make_float2(0.0, 0.0), thrust::plus<float2>());
    CENTER.x = newCenter.x / P_NUM;
    CENTER.y = newCenter.y / P_NUM;
    KERNEL_PUSH(CENTER, double2);
}

void k_update() {
    uchar4* screen;
    size_t size;
    CSC(cudaGraphicsMapResources(1, &res, 0));
    CSC(cudaGraphicsResourceGetMappedPointer((void**)&screen, &size, res));

    k_calc_fnc<<<dim3(16, 16), dim3(16, 16)>>>();
    k_calc_minmax();
    k_draw_map<<<dim3(16, 16), dim3(16, 16)>>>(screen);
    k_draw_particle<<<16, 16>>>(screen);
  
    if (STATE) {
        k_calc_lbest<<<16, 16>>>();
        k_calc_gbest();
        k_calc_particle<<<16, 16>>>(rand());
        k_calc_center();
    }
  
    CSC(cudaDeviceSynchronize());
    CSC(cudaGraphicsUnmapResources(1, &res, 0));
  
    glutPostRedisplay();
}


void k_processNormalKeys(unsigned char key, int x, int y) {
    switch (key) {
        case 'c':
            PSO_DT *= 0.7;
            break;
        case 'v':
            PSO_DT *= 1.4;
            break;
        case 'r':
            k_random_particle();
            break;
        case 'z':
            RADIUS = max(RADIUS * 0.7, 0.2);
            break;
        case 'x':
            RADIUS = RADIUS * 1.4;
            break;
        case ' ':
            STATE = !STATE;
            break;
        case 'd':
            CENTER.x += 0.5;
            break;
        case 'a':
            CENTER.x -= 0.5;
            break;
        case 'w':
            CENTER.y += 0.5;
            break;
        case 's':
            CENTER.y -= 0.5;
            break;
        case 'q':
            exit(0);
            break;
    }
    KERNEL_PUSH(PSO_DT, float);
    KERNEL_PUSH(RADIUS, double);
    KERNEL_PUSH(CENTER, double2);
}
