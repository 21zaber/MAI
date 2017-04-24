#include <cstdio>
#include <string>
#include <cassert>
#include <iostream>
#include <cstddef>
#include <vector>


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

double minor3x3(double m[3][3], int i, int j) {
	double arr[4];
	int len = 0;
	for (int row = 0; row < 3; row++) {
		for (int col = 0; col < 3; col++) {
			if (col == j || row == i) continue;
			arr[len++] = m[row][col];
		}
	}
	return arr[0] * arr[3] - arr[1] * arr[2];
}

double cof3x3(double m[3][3], int i, int j) {
    double mr = minor3x3(m, i, j);
    if ((i+j) % 2 == 1)
        mr *= -1;
    return mr;
}

double det3x3(double m[3][3]) {
	double res = 0;
	for (int col = 0; col < 3; col++) {
		res += m[0][col] * cof3x3(m, 0, col);
	}
	return res;
}

class IMG {
public:
	uint32_t w;
    uint32_t h;
    uint64_t size;
	uchar4 *data;

	IMG() : w(0), h(0), size(0), data(NULL) {}

	IMG(string path) {
		FILE *fin = fopen(path.c_str(), "rb");
		if (!fin) {
            cout << "Wrong file name " << path << "!\n";
			return;
		}
		fread(&w, sizeof(uint32_t), 1, fin);
		fread(&h, sizeof(uint32_t), 1, fin);
        size = w * h;
		data = new uchar4[size];
		fread(data, sizeof(uchar4), size, fin);
		fclose(fin);
	}
	~IMG() {
		if (data != NULL) {
			delete[] data;
		}
	}

	void toFile(string path) {
		FILE *fout = fopen(path.c_str(), "wb");
		if (!fout) {
            cout << "Wrong file name " << path << "!\n";
			return;
		}
		fwrite(&w, sizeof(uint32_t), 1, fout);
		fwrite(&h, sizeof(uint32_t), 1, fout);
		fwrite(data, sizeof(uchar4), size, fout);
		fclose(fout);
	}
};

//
// main programm
//



#define pixel uchar4
#define p(x, y) data[y*w + x]

vector<vector<pixel> > cls;
__constant__ double GPU_AVG[50][3];
__constant__ double GPU_INVERT_COV[50][3][3];


__device__ double mahalanobis(const pixel p, int ci) {
	double v[3] = {p.x - GPU_AVG[ci][0], 
                   p.y - GPU_AVG[ci][1], 
                   p.z - GPU_AVG[ci][2] 
                  };
	double tmp[3] = {0, 0, 0}, res = 0;
	for (int i = 0; i < 3; ++i) {
		for (int j = 0; j < 3; ++j) {
			tmp[i] += v[j] * GPU_INVERT_COV[ci][j][i];
		}
        res -= tmp[i] * v[i];
	}
	return res;
}


__device__ void classify(pixel &p, int cnum) {
	double mx = mahalanobis(p, 0);
	p.w = 0;
	for (char ci = 1; ci < cnum; ++ci) {
		double tmp = mahalanobis(p, ci);
		if (tmp > mx) {
			mx = tmp;
			p.w = ci;
		}
	}
}

__global__ void kernel(uchar4 *data, uint32_t w, uint32_t h, int cnum) {
	int idx = blockDim.x * blockIdx.x + threadIdx.x;
	int idy = blockDim.y * blockIdx.y + threadIdx.y;
	int offsetx = blockDim.x * gridDim.x;
	int offsety = blockDim.y * gridDim.y;

	for (int x = idx; x < w; x += offsetx) {
		for (int y = idy; y < h; y += offsety) {
			classify(p(x, y), cnum);
		}
	}
}

int main() {
int cnum = 0;
	string in, out;
	cin >> in >> out >> cnum;

    cls.resize(cnum, vector<pixel>());
    double cavg[cnum][3];
    double ccov[cnum][3][3];
    memset(cavg, 0, sizeof(double) * cnum * 3);
    memset(ccov, 0, sizeof(double) * cnum * 9);
	IMG img(in);
    uint32_t w = img.w; 

    for (int i = 0; i < cnum; ++i) {
        int csize, x, y;
        cin >> csize;
        for (int j = 0; j < csize; ++j) {
            cin >> x >> y;
            pixel p = img.p(x, y);
            cls[i].push_back(p);
            cavg[i][0] += p.x;    
            cavg[i][1] += p.y;    
            cavg[i][2] += p.z;    
        }
        for (int j = 0; j < 3; ++j) cavg[i][j] /= csize;
    }

	for (int c = 0; c < cnum; ++c) {
        int csize = cls[c].size();
		for (int i = 0; i < csize; ++i) {
			pixel p = cls[c][i];
			double coeff[3] = {p.x - cavg[c][0], 
                               p.y - cavg[c][1], 
                               p.z - cavg[c][2]
                              };

			for (int r = 0; r < 3; ++r) {
				for (int s = 0; s < 3; ++s) {
					ccov[c][r][s] += coeff[r] * coeff[s];
				}
			}
		}
        for (int r = 0; r < 3; ++r) {
            for (int s = 0; s < 3; ++s) {
				ccov[c][r][s] /= csize - 1;
			}
		}
		double det = det3x3(ccov[c]);
        double icov[3][3];
        for (int r = 0; r < 3; ++r) {
            for (int s = 0; s < 3; ++s) {
				if (det == 0) {
					icov[s][r] = (r == s ? 1 : 0);
				} else {
					icov[s][r] = cof3x3(ccov[c], r, s) / det;
				}
			}
		}
        for (int r = 0; r < 3; ++r) {
            for (int s = 0; s < 3; ++s) {
				ccov[c][r][s] = icov[r][s];
			}
		}
	}
	uchar4 *result;
	CSC(cudaMemcpyToSymbol(GPU_AVG, cavg, sizeof(double) * cnum * 3));
	CSC(cudaMemcpyToSymbol(GPU_INVERT_COV, ccov, sizeof(double) * cnum * 9));
	CSC(cudaMalloc(&result, sizeof(uchar4) * img.size));
	CSC(cudaMemcpy(result, img.data, sizeof(uchar4) * img.size, cudaMemcpyHostToDevice));

	kernel<<<dim3(16, 16), dim3(16, 16)>>>(result, img.w, img.h, cnum);

	CSC(cudaMemcpy(img.data, result, sizeof(uchar4) * img.size, cudaMemcpyDeviceToHost));
	CSC(cudaFree(result));

	img.toFile(out);
}
