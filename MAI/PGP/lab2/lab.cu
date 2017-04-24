#include <cstdio>
#include <string>
#include <cassert>
#include <iostream>
#include <cstddef>
//#include <cstdint>


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

//
// main programm
//

uchar4 *readimg(string path, uint32_t &w, uint32_t &h) {
    FILE *f = fopen(path.c_str(), "rb");
    fread(&w, sizeof(uint32_t), 1, f);
    fread(&h, sizeof(uint32_t), 1, f);
    uint64_t size = w * h;     
    uchar4 *data = new uchar4[size];
    fread(data, sizeof(uchar4), size, f);
    fclose(f);
    return data;
}

void writeimg(string path, uchar4 *data, const uint32_t w, const uint32_t h) {
    FILE *fout = fopen(path.c_str(), "wb");
    fwrite(&w, sizeof(uint32_t), 1, fout);
    fwrite(&h, sizeof(uint32_t), 1, fout);
    uint64_t size = w * h;     
    fwrite(data, sizeof(uchar4), size, fout);
    fclose(fout);
    delete[] data;
}

__device__ uint8_t medc(uint16_t *cnt, int mid) {
	int sum = 0, i = -1;
	while (i < 256 && sum <= mid) sum += cnt[++i];
	return i;
}

texture<uchar4, 2, cudaReadModeElementType> tex;

__device__ void medpx(uchar4 &px, int x0, int y0, uint32_t radius, uint32_t w, uint32_t h) {
	uchar4 p;
	uint16_t cnt[3][256];

    memset(cnt, 0, 3 * 256 * sizeof(uint16_t));

    int rd = (int)radius;

    int fx = max(0, x0-rd), tx = min(w, x0+rd+1);
    int fy = max(0, y0-rd), ty = min(h, y0+rd+1);
	int n = (tx - fx) * (ty - fy) / 2;

	for (int x = fx; x < tx; ++x) {
	    for (int y = fy; y < ty; ++y) {
			p = tex2D(tex, x, y);
			++cnt[0][p.x];
			++cnt[1][p.y];
			++cnt[2][p.z];
		}
	}


	px.x = medc(cnt[0], n);
	px.y = medc(cnt[1], n);
	px.z = medc(cnt[2], n);
	px.w = tex2D(tex, x0, y0).w;
}
                                        
__global__ void kernel(uchar4 *dst, uint32_t w, uint32_t h, uint32_t radius) {
	int idx = blockDim.x * blockIdx.x + threadIdx.x;
	int idy = blockDim.y * blockIdx.y + threadIdx.y;
	int offsetx = blockDim.x * gridDim.x;
	int offsety = blockDim.y * gridDim.y;

	for (int x = idx; x < w; x += offsetx) {
		for (int y = idy; y < h; y += offsety) {
			 medpx(dst[y * w + x], x, y, radius, w, h);
		}
	}
}


int main() {
	string in, out;
	uint32_t radius, w, h;
	cin >> in >> out >> radius;

    uchar4 *data = readimg(in, w, h);
    uint64_t size = w * h;

	cudaArray *arr;
	cudaChannelFormatDesc ch = cudaCreateChannelDesc<uchar4>();
	CSC(cudaMallocArray(&arr, &ch, w, h));
	CSC(cudaMemcpyToArray(arr, 0, 0, data, sizeof(uchar4) * size, cudaMemcpyHostToDevice));

	tex.addressMode[0] = cudaAddressModeClamp;
	tex.addressMode[1] = cudaAddressModeClamp;
	tex.channelDesc = ch;
	tex.filterMode = cudaFilterModePoint;
	tex.normalized = false;
	CSC(cudaBindTextureToArray(tex, arr, ch));

	uchar4 *result;
	CSC(cudaMalloc(&result, sizeof(uchar4) * size));

	kernel<<<dim3(16, 16), dim3(16, 16)>>>(result, w, h, radius);
	CSC(cudaGetLastError());
	CSC(cudaMemcpy(data, result, sizeof(uchar4) * size, cudaMemcpyDeviceToHost));

	CSC(cudaUnbindTexture(tex));
	CSC(cudaFreeArray(arr));
	CSC(cudaFree(result));

	writeimg(out, data, w, h);
}
