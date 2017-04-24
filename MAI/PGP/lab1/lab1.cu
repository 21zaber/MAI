#include <iostream>
#include <cstdio>
#include <iomanip>

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


double* dmalloc(int n) {
	double *d_arr;
	CSC(cudaMalloc(&d_arr, sizeof(double) * n));
	CSC(cudaGetLastError());
	return d_arr;
}

void dfree(double *darr) {
    CSC(cudaFree(darr));
	CSC(cudaGetLastError());
}

void hdmemcpy(double *arr, double *darr, int n) {
	CSC(cudaMemcpy(darr, arr, sizeof(double) * n, cudaMemcpyHostToDevice));
	CSC(cudaGetLastError());
}

void dhmemcpy(double *arr, double *darr, int n) {
	CSC(cudaMemcpy(arr, darr, sizeof(double) * n, cudaMemcpyDeviceToHost));
	CSC(cudaGetLastError());
}


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


__global__ void kernel(double *darr, int n) {
	int idx = blockIdx.x * blockDim.x + threadIdx.x;
	int offset = gridDim.x * blockDim.x;

	while (idx < n) {
		darr[idx] *= darr[idx];
		idx += offset;
	}
}

int main() {
	cout.precision(10);
	cout.setf(ios::scientific);

	int n;
	cin >> n;

	double *arr = new double[n];
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}

	double *darr = dmalloc(n);
	hdmemcpy(arr, darr, n);

#ifdef TIMER
    timer_start();
#endif
    
	kernel<<<256, 256>>>(darr, n);

#ifdef TIMER
    timer_end();
#endif

	dhmemcpy(arr, darr, n);
	dfree(darr);

	for (int i = 0; i < n; i++) {
		cout << arr[i] << ' ';
	}
	cout << endl;
}
