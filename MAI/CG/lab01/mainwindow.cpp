#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "cmath"
#include "QPainter"
//#include "point.h"
#include "matrix.h"
#include <QMouseEvent>
#include "fstream"
#include "math.h"
//#include "stdlib.h"


MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    alpha(0.13),
    beta(-0.1),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow(){
    delete ui;
}

double a = 30, b = 30, c = 30;
double step = 0.1, st = -1, fn = 1, scale = 1;
double mousex, mousey, oldalpha, oldbeta;
int minx = 15, miny = 15, maxx, maxy;


Point f(double t){
    //x = a * cos(t)
    //y = b * sin(t)
    //z = c * t
    return Point(a * cos(t), b * sin(t), c * t);
}

Point g(double t){
    //x = a * cos(t) - b * cos(c * t)
    //y = a * sin(t) - b * sin(c * t)
    //z = cos(sqrt(x * x + y * y))
    double x = a * cos(t) - b * cos(c * t);
    double y = a * sin(t) - b * sin(c * t);
    double z = b * cos(sqrt(x * x / (a * a) + y * y / (a * a)));
    return Point(x, y, z);
}

Point (*function)(double) = f;

void drawline(QPainter &painter, Point a, Point b){
    if (a.x() > minx and b.x() > minx and
        a.x() < maxx and b.x() < maxx and
        a.y() > miny and b.y() > miny and
        a.y() < maxy and b.y() < maxy)
        painter.drawLine(a.x(), a.y(), b.x(), b.y());
}

void drawfunc(QPainter &p, Point (*f)(double), Matrix t){
    if ((fn - st) / step > 100000)
        return;
    Point prev = f(st);
    for (double i = st + step; i < fn; i += step){
        Point now = t * (f(i) * scale);
        drawline(p, now, prev);
        prev = now;
    }
}

void drawOXYZ(QPainter &painter, Matrix t){
    painter.fillRect(minx, miny, maxx - minx, maxy - miny, Qt::white);
    Point center((minx + maxx) / 2, (miny + maxy) / 2, 0);
    double ln = std::min((maxx - minx), (maxy - miny)) / 3;
    Point ox(ln, 0, 0), oy(0, ln, 0), oz(0, 0, ln);
    ox = t * ox;
    oy = t * oy;
    oz = t * oz;
    painter.setPen(Qt::red);
    painter.drawLine(center.x(), center.y(), ox.x(), ox.y());
    painter.setPen(Qt::blue);
    painter.drawLine(center.x(), center.y(), oy.x(), oy.y());
    painter.setPen(Qt::green);
    painter.drawLine(center.x(), center.y(), oz.x(), oz.y());
    painter.setPen(Qt::black);
}

void MainWindow::paintEvent(QPaintEvent *) {
    QPainter painter(this);
    maxx = this->width() - 150;
    maxy = this->height() - 35;
    Point center((minx + maxx) / 2, (miny + maxy) / 2, 0);
    Matrix t = Matrix().move(center) *
               Matrix().rotateX(beta) *
               Matrix().rotateY(alpha);

    drawOXYZ(painter, t);
    drawfunc(painter, function, t);
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

void MainWindow::on_spinBoxA_valueChanged(int arg1){
    a = arg1;
    update();
}

void MainWindow::on_spinBoxB_valueChanged(int arg1){
    b = arg1;
    update();
}

void MainWindow::on_spinBoxC_valueChanged(int arg1){
    c = arg1;
    update();
}

void MainWindow::on_doubleSpinBox_valueChanged(double arg1){
    if (arg1 > 0.001)
        step = arg1;
    update();
}

void MainWindow::on_doubleSpinBox_2_valueChanged(double arg1){
    st = arg1;
    update();
}

void MainWindow::on_doubleSpinBox_3_valueChanged(double arg1){
    fn = arg1;
    update();
}

void MainWindow::on_doubleSpinBox_4_valueChanged(double arg1){
    if (arg1 > 0)
        scale = arg1;
    update();
}

void MainWindow::on_radioButton_clicked(){
    function = f;
    update();
}

void MainWindow::on_radioButton_2_clicked(){
    function = g;
    update();
}

void MainWindow::on_CloseButton_clicked(){
    this->destroy();
}
