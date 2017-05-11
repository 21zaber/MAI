#include <cstdio>
#include <string>
#include <cassert>
#include <iostream>
#include <cstddef>
#include <vector>                 
#include <thrust/device_vector.h>
#include <thrust/extrema.h>
#include <limits>

using namespace std;

#define int8_t  char
#define int16_t short
#define int32_t int
#define int64_t long long

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

const int BLOCK_SIZE = 1024;
const int GRID_SIZE = 16384;
//const int64_t INF = 2100000000;
const int64_t INF = 2147483647;

__global__ void k_blocksort(int64_t *arr, int len) {
    if (blockIdx.x * BLOCK_SIZE >= len) {
        return;
    }

    __shared__ int64_t block[BLOCK_SIZE];
    int idx = threadIdx.x * 2;
    int offset = blockIdx.x * BLOCK_SIZE;
    int nstep = BLOCK_SIZE / 2;

   // printf("offset %d", offset);

    block[idx] =  arr[offset + idx];
    block[idx+1] = arr[offset + idx+1];

    int64_t tmp;
 //         __syncthreads();
 // 		if (idx < 10)
 //         printf("%d, %d\n", idx, block[idx]);
    for (int k = 0; k < nstep; k++) {
        for (int i = idx+1; i < idx+3; ++i){
            __syncthreads();
            if (i < BLOCK_SIZE) {
                if (block[i-1] > block[i]) {
			//		printf("swap %d %d\n", i-1, i);
                    tmp = block[i-1];
                    block[i-1] = block[i];
                    block[i] = tmp;
                }
            }
        }
    }

    __syncthreads();
    arr[offset + idx] = block[idx];
    arr[offset + idx+1] = block[idx+1];
}


__global__ void k_merge(int64_t *arr, int len, bool odd) {
    int offset = blockIdx.x * BLOCK_SIZE * 2;
    int idx = threadIdx.x;
    int64_t tmp;

    if (odd) offset += BLOCK_SIZE; 

    if (offset + BLOCK_SIZE * 2 > len) return; 

    __shared__ int64_t block[BLOCK_SIZE * 2];

    int idt = 2 * idx;
    block[idt] =  arr[offset + idt];
    block[idt+1] = arr[offset + idt+1];

    __syncthreads();
    idt = BLOCK_SIZE * 2 - idx - 1;
    if (idx < BLOCK_SIZE && block[idx] > block[idt]) {
        tmp = block[idx];
        block[idx] = block[idt];
        block[idt] = tmp;
    }


    int step = BLOCK_SIZE / 2;
    while (step != 0) {
        __syncthreads();
        idt = idx;

        if ((idx / step) % 2 == 1) {
            idt -= step - BLOCK_SIZE;
        }
        if (block[idt] > block[idt + step]) {
            tmp = block[idt];
            block[idt] = block[idt+step];
            block[idt+step] = tmp;
        }
        step /= 2;
    }

    idt = 2 * idx;
    __syncthreads();
    arr[offset + idt] = block[idt];
    arr[offset + idt+1] = block[idt+1];
}


int main() {
    time_t tm, tmc;
    time(&tm);

    time(&tmc);
  //  fprintf(stderr, "%d: %f\t", __LINE__, difftime(tmc, tm));
    time(&tm);
    int n;
    fread(&n, sizeof(int), 1, stdin);

    fprintf(stderr, "n=%d\t", n);

    int rn = n;
    if (n % BLOCK_SIZE != 0) {
        n += BLOCK_SIZE - n % BLOCK_SIZE;
    }

    int64_t *arr = new int64_t[n];
    int l;
   // fprintf(stderr, "\n");
    for (int i = 0; i < n; i++) {
        l = INF;
        if (i < rn) {
            fread(&l, sizeof(int), 1, stdin);
            //fprintf(stderr, "%d ", l);
        }
        arr[i] = l;
    }
    //fprintf(stderr, "\n");
    

    time(&tmc);
  //  fprintf(stderr, "%d: %f\t", __LINE__, difftime(tmc, tm));
    time(&tm);

    int64_t *darr;
    CSC(cudaMalloc(&darr, sizeof(int64_t) * n));
    CSC(cudaMemcpy(darr, arr, sizeof(int64_t) * n, cudaMemcpyHostToDevice));

    k_blocksort<<<GRID_SIZE, BLOCK_SIZE / 2>>>(darr, n);
    CSC(cudaGetLastError());

  //CSC(cudaMemcpy(arr, darr, sizeof(int64_t) * n, cudaMemcpyDeviceToHost));
  //cout << "after sort" << endl;
  //for (int i = 0; i < rn; i++) {
  //    l = (int)arr[i];
  //    cout << l << " ";
  //    //fwrite(&l, sizeof(int), 1, stdout);
  //}
  //cout << endl;

    time(&tmc);
  //  fprintf(stderr, "%d: %f\t", __LINE__, difftime(tmc, tm));
    time(&tm);

	fprintf(stderr, "num of steps %d\n", n / BLOCK_SIZE);

    if (n > BLOCK_SIZE) {
        for (int step = 0; step < n / BLOCK_SIZE; step++) {
            k_merge<<<GRID_SIZE, BLOCK_SIZE>>>(darr, n, step & 1);
            CSC(cudaGetLastError());
  //CSC(cudaMemcpy(arr, darr, sizeof(int64_t) * n, cudaMemcpyDeviceToHost));
  //cout << "after step" << endl;
  //for (int i = 0; i < rn; i++) {
  //    l = (int)arr[i];
  //    cout << l << " ";
  //    //fwrite(&l, sizeof(int), 1, stdout);
  //}
  //cout << endl;
        }
    }

    CSC(cudaMemcpy(arr, darr, sizeof(int64_t) * rn, cudaMemcpyDeviceToHost));
    CSC(cudaFree(darr));

    time(&tmc);
  //  fprintf(stderr, "%d: %f\t", __LINE__, difftime(tmc, tm));
    time(&tm);

    for (int i = 0; i < rn; i++) {
        l = (int)arr[i];
      //  cout << l << " ";
        fwrite(&l, sizeof(int), 1, stdout);
    }
   // cout << endl;

    time(&tmc);
   // fprintf(stderr, "%d: %f\t", __LINE__, difftime(tmc, tm));
    time(&tm);
}
