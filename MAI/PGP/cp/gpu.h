#pragma once

#include "conf.h"

#include <GL/glew.h>
#include <GL/freeglut.h>

#include <cuda.h>
#include <cuda_runtime.h>
#include <cuda_gl_interop.h>
#include <curand_kernel.h>

#include <thrust/device_vector.h>
#include <thrust/extrema.h>
#include <thrust/reduce.h>


// P = plane, S = screen 
#define k_point_S2Px(xa) ((float)(xa-(WIDTH/2)) * ((float)K_RADIUS / WIDTH) * 2 + K_CENTER.x)
#define k_point_S2Py(ya) ((float)(ya-(HEIGHT/2)) * ((float)K_RADIUS / HEIGHT) * 2 + K_CENTER.y)

#define k_point_P2Sx(xa) (((float)xa - K_CENTER.x) * ((float)WIDTH / K_RADIUS) / 2 + WIDTH / 2)
#define k_point_P2Sy(ya) (((float)ya - K_CENTER.y) * ((float)HEIGHT / K_RADIUS) / 2 + HEIGHT / 2)

KERNEL_MIRROR(float, PSO_DT) = PSO_DT_DEFAULT;

KERNEL_MIRROR(float, F_MAX);
KERNEL_MIRROR(float, F_MIN);
KERNEL_MIRROR(int2, F_X) = make_int2(-5, 5);
KERNEL_MIRROR(int2, F_Y) = make_int2(-5, 5);

// Current camera position
KERNEL_MIRROR(double, RADIUS) = 3;
KERNEL_MIRROR(double2, CENTER) = make_double2(0, 0);

#define RUN 1;
#define STOP 0;
int STATE = STOP;

#define CSC(call) {                                                                                                   \
    cudaError err = call;                                                                                             \
    if (err != cudaSuccess) {                                                                                         \
        fprintf(stderr, "CUDA error in file '%s' in line %i: %s.\n", __FILE__, __LINE__, cudaGetErrorString(err));    \
        exit(1);                                                                                                      \
    }                                                                                                                 \
} while (0)

#define KERNEL_PUSH(val, type) CSC(cudaMemcpyToSymbol(K_ ## val, &val, sizeof(type))) 

__constant__ float2 *velocity;
__constant__ float2 *points;
__constant__ float3 *lbest;
__constant__ float3 gbest;
__constant__ float *fnc;

struct cudaGraphicsResource *res;  

//
// INIT functions
//

void k_random_particle() {
    srand(time(0));
    float2 *p = new float2[P_NUM];
    float2 *v = new float2[P_NUM];
    float3 *lb = new float3[P_NUM];
    void *tmp;

    for (int i = 0; i < P_NUM; i++) {
        p[i].x = ((float)rand() / (float)(RAND_MAX)) * (F_X.y - F_X.x) + F_X.x;
        p[i].y = ((float)rand() / (float)(RAND_MAX)) * (F_Y.y - F_Y.x) + F_Y.x;
        //v[i] = make_float2(0, 0);
        v[i] = make_float2(((float)rand() / (float)(RAND_MAX)), ((float)rand() / (float)(RAND_MAX)));
        lb[i] = make_float3(0, 0, INF);
    }

    CSC(cudaMalloc(&tmp, sizeof(float2) * P_NUM));
    CSC(cudaMemcpy(tmp, p, sizeof(float2) * P_NUM, cudaMemcpyHostToDevice));
    CSC(cudaMemcpyToSymbol(points, &tmp, sizeof(float2*)));
    delete[] p;

    CSC(cudaMalloc(&tmp, sizeof(float2) * P_NUM));
    CSC(cudaMemcpy(tmp, v, sizeof(float2) * P_NUM, cudaMemcpyHostToDevice));
    CSC(cudaMemcpyToSymbol(velocity, &tmp, sizeof(float2*)));
    delete[] v;

    CSC(cudaMalloc(&tmp, sizeof(float3) * P_NUM));
    CSC(cudaMemcpy(tmp, lb, sizeof(float3) * P_NUM, cudaMemcpyHostToDevice));
    CSC(cudaMemcpyToSymbol(lbest, &tmp, sizeof(float3*)));
    delete[] lb;

    float3 h_gbest = make_float3(0.0, 0.0, INF);
    CSC(cudaMemcpyToSymbol(gbest, &h_gbest, sizeof(float3)));

    CSC(cudaMalloc(&tmp, sizeof(float) * WIDTH * HEIGHT));
    CSC(cudaMemcpyToSymbol(fnc, &tmp, sizeof(float*)));
}

void k_init() {
    KERNEL_PUSH(PSO_DT, float);
    KERNEL_PUSH(F_X, int2);
    KERNEL_PUSH(F_Y, int2);
    KERNEL_PUSH(RADIUS, double);
    KERNEL_PUSH(CENTER, double2);
    k_random_particle();
}

__global__ void k_draw_map(uchar4* data);
__global__ void k_calc_fnc();
__global__ void k_draw_particle(uchar4* data);
__global__ void k_calc_lbest();
__global__ void k_calc_particle(unsigned long long seed);

void k_calc_center();
void k_calc_minmax();
void k_calc_gbest();

void k_processNormalKeys(unsigned char key, int x, int y);
void k_update();


















