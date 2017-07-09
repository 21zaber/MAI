#include "conf.h"
//#include "gpu.h"

#include <stdio.h>
#include <cmath>
#include <cstdlib>
#include <ctime>

#include <GL/glew.h>
#include <GL/freeglut.h>
#include <cuda_gl_interop.h>

void display() {
    glClearColor(0.0, 0.0, 0.0, 1.0);
    glClear(GL_COLOR_BUFFER_BIT);
    glDrawPixels(WIDTH, HEIGHT, GL_RGBA, GL_UNSIGNED_BYTE, 0);
    glutSwapBuffers();
}

int main(int argc, char** argv) {
    k_init();

    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA);
    glutInitWindowSize(WIDTH, HEIGHT);
    glutCreateWindow("CP N.I.Zabarin");

    glutIdleFunc(k_update);
    glutDisplayFunc(display);
    glutKeyboardFunc(k_processNormalKeys);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(0.0, (GLdouble)WIDTH, 0.0, (GLdouble)HEIGHT);

    glewInit();

    GLuint vbo;
    glGenBuffers(1, &vbo);
    glBindBuffer(GL_PIXEL_UNPACK_BUFFER_ARB, vbo);
    glBufferData(GL_PIXEL_UNPACK_BUFFER_ARB, WIDTH * HEIGHT * sizeof(uchar4), NULL, GL_DYNAMIC_DRAW);

    CSC(cudaGraphicsGLRegisterBuffer(&res, vbo, cudaGraphicsMapFlagsWriteDiscard));

    glutMainLoop();

    CSC(cudaGraphicsUnregisterResource(res));

    glBindBuffer(1, vbo);
    glDeleteBuffers(1, &vbo);
}
