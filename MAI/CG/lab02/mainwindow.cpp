#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "object.h"
#include <QMouseEvent>
#include <math.h>
#include <canvas.h>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    alpha(0.13),
    beta(-0.1),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}

double a = 30;
double step = 0.5, st = -M_PI, fn = M_PI, scale = 1;
double mousex, mousey, oldalpha, oldbeta;
int minx = 15, miny = 15, maxx, maxy;
int sz = 100;
const double eps = 0.000000001;

Object getsq(){
    Object *ob = new Object;
    ob->addpoint(0, 0, 0);
    ob->addpoint(0, sz, 0);
    ob->addpoint(sz, sz, 0);
    ob->addpoint(sz, 0, 0);
    ob->addpoint(sz, 0, sz);
    ob->addpoint(0, 0, sz);
    ob->addpoint(0, sz, sz);
    ob->addpoint(sz, sz, sz);

    ob->addfacet(0, 1, 2, 3);
    ob->addfacet(2, 7, 4, 3);
    ob->addfacet(1, 0, 5, 6);
    ob->addfacet(1, 6, 7, 2);
    ob->addfacet(0, 3, 4, 5);
    ob->addfacet(7, 6, 5, 4);
    return *ob;
}

Object getpov(){
    int n = int((fn - st + eps) / step);
    if (n > 600){
        return *new Object;
    }
    Object *ob = new Object;
    /*for (double r = st; r < fn; r += step){
        for (double angle = st; angle < fn; angle += step){
            ob->addpoint(sz * r * sin(angle), sz * r * cos(angle), sz * a * r * r);
        }
    }*/
    int t = 0;
    for (double x = st; x < fn; x += step){
        ++t;
        for (double y = st; y < fn; y += step){
            ob->addpoint(sz * sz * x, sz * sz * y, sz * a * (x * x + y * y));
        }
    }
    for (int i = 0; i < t - 1; ++i){
        for (int j = 0; j < t - 1; ++j){
            vector<int> q(4);
            q[3] = (i + 0) * t + j + 0;
            q[2] = (i + 1) * t + j + 0;
            q[1] = (i + 1) * t + j + 1;
            q[0] = (i + 0) * t + j + 1;
            ob->addfacet(q);
        }
    }
    return *ob;
}

Object getprism(){
    Object *ob = new Object;
    ob->addpoint(0 * sz,  0 * sz, 0 * sz);
    ob->addpoint(0 * sz,  0 * sz, 2 * sz);
    ob->addpoint(2 * sz, -2 * sz, 0 * sz);
    ob->addpoint(2 * sz, -2 * sz, 4 * sz);
    ob->addpoint(4 * sz, -2 * sz, 0 * sz);
    ob->addpoint(4 * sz, -2 * sz, 6 * sz);
    ob->addpoint(6 * sz, -1 * sz, 0 * sz);
    ob->addpoint(6 * sz, -1 * sz, 8 * sz);
    ob->addpoint(5 * sz,  2 * sz, 0 * sz);
    ob->addpoint(5 * sz,  2 * sz, 7 * sz);
    ob->addpoint(2 * sz,  2 * sz, 0 * sz);
    ob->addpoint(2 * sz,  2 * sz, 4 * sz);

    ob->addfacet(0, 1, 3, 2);
    ob->addfacet(2, 3, 5, 4);
    ob->addfacet(4, 5, 7, 6);
    ob->addfacet(6, 7, 9, 8);
    ob->addfacet(8, 9, 11, 10);
    ob->addfacet(10, 11, 1, 0);
    vector<int> t(6), b(6);
    t[0] = 0; t[1] = 2;
    t[2] = 4; t[3] = 6;
    t[4] = 8; t[5] = 10;

    b[5] = 1; b[4] = 3;
    b[3] = 5; b[2] = 7;
    b[1] = 9; b[0] = 11;

    ob->addfacet(t);
    ob->addfacet(b);

    return *ob;
}

Object (*function)() = getsq;

Canvas canv;

void MainWindow::paintEvent(QPaintEvent *){
    maxx = width() - 190;
    maxy = height() - 35;
    Point center((minx + maxx) / 2, (miny + maxy) / 2, 0);
    Matrix matrix = Matrix().move(center) *
                    Matrix().rotateX(beta) *
                    Matrix().rotateY(alpha);

    Object ob = function();
    QPainter painter(this);

    canv.setPainter(painter);
    canv.setSize(this->width(), this->height());
    canv.setMatrix(matrix);
    canv.clearObjects();
    canv.addObject(ob);
    canv.drawAll();
}

void MainWindow::mousePressEvent(QMouseEvent *e){
    mousex = e->x();
    mousey = e->y();
    oldalpha = alpha;
    oldbeta = beta;
}

void MainWindow::mouseMoveEvent(QMouseEvent *e){
    this->alpha = oldalpha + (e->x() - mousex) * 0.005;
    this->beta = oldbeta + (e->y() - mousey) * 0.005;
    update();
}

void MainWindow::on_pushButton_clicked(){
    this->destroy();
}

void MainWindow::on_comboBox_currentIndexChanged(int index){
    if (index == 0){//Cube
        function = getsq;
        sz = 100;
        alpha = 1;
        beta = 1;
    }
    if (index == 2){//prism
        function = getprism;
        sz = 50;
        alpha = 1;
        beta = 1;
    }
    if (index == 1){//surface
        function = getpov;
        sz = 8;
        a = 2;
        step = 0.5;
        st = -5;
        fn = 5;
        alpha = 2;
        beta = 0.5;
    }
    update();
}

void MainWindow::on_doubleSpinBox_valueChanged(double arg1){
    a = arg1;
    update();
}

void MainWindow::on_doubleSpinBox_2_valueChanged(double arg1){
    sz = arg1;
    update();
}

void MainWindow::on_doubleSpinBox_3_valueChanged(double arg1){
    st = arg1;
    update();
}

void MainWindow::on_doubleSpinBox_4_valueChanged(double arg1){
    fn = arg1;
    update();
}

void MainWindow::on_doubleSpinBox_5_valueChanged(double arg1){
    if (arg1 < 0.001) return;
    step = arg1;
    update();
}
