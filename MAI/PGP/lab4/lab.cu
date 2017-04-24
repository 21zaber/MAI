#include <cstdio>
#include <string>
#include <cassert>
#include <iostream>
#include <cstddef>
#include <vector>                 
#include <thrust/device_vector.h>
#include <thrust/extrema.h>


#define uint8_t  unsigned char
#define uint16_t unsigned short
#define uint32_t unsigned int
#define uint64_t unsigned long long

using namespace std;
//
// DEFAULt functions for work with cuda
//

#define CSC(call) do { \
	cudaError_t res = call;	\
	if (res != cudaSuccess) { \
		fprintf(stderr, "CUDA Error in %s:%d: %s\n", __FILE__, __LINE__, cudaGetErrorString(res)); \
		exit(0); \
	} \
} while (0)


cudaEvent_t start, stop;
float t;

void time_start() {
	CSC(cudaEventCreate(&start));
	CSC(cudaEventCreate(&stop));
	CSC(cudaEventRecord(start, 0));
}

void time_end() {
	CSC(cudaGetLastError());
	CSC(cudaEventRecord(stop, 0));
	CSC(cudaEventSynchronize(stop));
	CSC(cudaEventElapsedTime(&t, start, stop));	
	printf("time = %f\n", t);
	CSC(cudaEventDestroy(start));
	CSC(cudaEventDestroy(stop));
}

//
// main programm
//



//  __global__ void kernel(uchar4 *data, uint32_t w, uint32_t h, int cnum) {
//      int idx = blockDim.x * blockIdx.x + threadIdx.x;
//      int idy = blockDim.y * blockIdx.y + threadIdx.y;
//      int offsetx = blockDim.x * gridDim.x;
//      int offsety = blockDim.y * gridDim.y;
//
//      for (int x = idx; x < w; x += offsetx) {
//          for (int y = idy; y < h; y += offsety) {
//              classify(p(x, y), cnum);
//          }
//      }
//  }
//

#define get(m, x, y) m[y*n + x]
#define gett(m, x, y) get(m, y, x)
#define getl(m, x, y) gett(m, x, y)
#define getu(m, x, y) gett(m, x, y)

struct cmpr {
    __host__ __device__ bool operator()(double a, double b) {
        return fabs(a) < fabs(b);
    }
};

__global__ void k_swapcolumns(double *dm, const uint32_t n, const uint32_t fr, const uint32_t to) {
    int idx = blockDim.x * blockIdx.x + threadIdx.x;
    int offsetx = blockDim.x * gridDim.x;
    double tmp = 0;

    for (int i = idx; i < n; i += offsetx) {
        tmp = get(dm, i, fr);
        get(dm, i, fr) = get(dm, i, to);
        get(dm, i, to) = tmp;
    }
}

__global__ void k_lucol(double *dm, const uint32_t n, const uint32_t i) {
    int idx = blockDim.x * blockIdx.x + threadIdx.x;
    int offsetx = blockDim.x * gridDim.x;

    for(int j = idx; j < n; j += offsetx) {
        if (j <= i) continue;

        for (int k = 0; k < i; ++k) {
            getu(dm, i, j) -= getl(dm, i, k) * getu(dm, k, j);
        }
        for (int k = 0; k < i; ++k) {
            getl(dm, j, i) -= getl(dm, j, k) * getu(dm, k, i);
        }
        getl(dm, j, i) /= get(dm, i, i);
    }
}

int main() {
    cout.precision(10);
    cout.setf(ios::scientific);
    
    int n;
    cin >> n;
    int size = n * n;
    double hm[size];
    int swaps[n];

    for (int i = 0; i < n; ++i) {
        swaps[i] = i;
        for (int j = 0; j < n; ++j) {
            cin >> gett(hm, i, j); // transpose of original matrix 
        } 
    }
    double *dm = NULL;
    CSC(cudaMalloc(&dm, sizeof(double) * size));
    CSC(cudaMemcpy(dm, hm, sizeof(double) * size, cudaMemcpyHostToDevice));

    for (int r = 0; r < n-1; ++r) {
        // find a max in row(columns) using thrust
        thrust::device_ptr<double> dp = thrust::device_pointer_cast(dm + r*n + r);
        thrust::device_ptr<double> mp = thrust::max_element(dp, dp + n - r, cmpr());
        int to = r + mp - dp, tmp;
        tmp = swaps[to], swaps[to] = swaps[r], swaps[r] = tmp;
        k_swapcolumns<<<256, 256>>>(dm, n, r, to);
        k_lucol<<<256, 256>>>(dm, n, r);
    }
    
    CSC(cudaMemcpy(hm, dm, sizeof(double) * size, cudaMemcpyDeviceToHost));
    CSC(cudaFree(dm));

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cout << gett(hm, i, j) << ' '; 
        } 
        cout << endl;
    }
    
    for (int i = 0; i < n; ++i) {
        cout << swaps[i] << ' ';
    }

    cout << endl;
}
