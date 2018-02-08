#pragma once

#define KERNEL_MIRROR(type, name) __constant__ type K_##name; type name

//
// Configuration
//

// Customization part
const int WIDTH =  1200;
const int HEIGHT = 700;
const int POINT_SIZE = 2;
const int P_NUM = 500;

// Formula's coefs
#define PSO_A1 0.1   // local coef
#define PSO_A2 0.01   // global coef
#define PSO_W  1.0
#define PSO_REP 1.0
#define PSO_DT_DEFAULT 1.0


// Function
#define Himmelblau(x, y) ((x*x + y - 11)*(x*x + y - 11) + (x + y*y - 7)*(x + y*y - 7))
#define Parabola(x, y) (x*x + y*y)
#define my_func(x, y) (sin((x+y)*0.001)*(x*x + y - 11)*(x*x + y - 11) + cos((x+y)*0.001)*(x + y*y - 7)*(x + y*y - 7))
//#define F(x, y) my_func(x, y)
#define F(x, y) Himmelblau(x, y)
//#define F(x, y) Parabola(x, y)

#define INF 1000.0 * 1000.0 * 1000.0

