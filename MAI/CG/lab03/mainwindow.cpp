#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "object.h"
#include <QMouseEvent>
#include <math.h>
#include <canvas.h>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    alpha(-3.6),
    beta(-2.1),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}

double a = 100, b = 100;
double step = 0.07, st = -M_PI, fn = M_PI, scale = 1;
double mousex, mousey, oldalpha, oldbeta;
int minx = 15, miny = 15, maxx, maxy;
//int sz = 100;
const double eps = 0.000000001;
double ar = 0.1, ag = 0.1, ab = 0.2;
double dr = 0.3, dg = 0.3, db = 0.3;
double sr = 0.5, sg = 0.5, sb = 0.0, specpow = 30;

Object getfirst(){
    Object *ob = new Object;
    double r = a, h = b;
    int count = 0;
    for (double al = 0; al < 2 * M_PI; al += step, ++count){
        ob->addpoint(r * sin(al), r * cos(al), - h / 2);
        ob->addpoint(r * sin(al), r * cos(al), h / 2);
    }
    ob->addpoint(r * sin(0), r * cos(0), - h / 2);
    ob->addpoint(r * sin(0), r * cos(0), h / 2);
    vector<int> top, bot, side;
    for (int i = 0; i < count; ++i){
        bot.push_back(2 * i);
        top.push_back(2 * count - 2 * i - 1);
        side.clear();
        side.push_back(2 * i + 0);
        side.push_back(2 * i + 1);
        side.push_back(2 * i + 3);
        side.push_back(2 * i + 2);
        ob->addfacet(side);
    }
    ob->addfacet(bot);
    ob->addfacet(top);
    return *ob;
}

Object getsecond(){
    Object *ob = new Object;
    double R = a;
    double r = b;
    //(R + rcos(a))cos(b)
    //(R + rcos(a))sin(b)
    //rsin(a)
    int count = 0, n = 0;
    for (double alpha = 0; alpha < M_PI * 2; alpha += step, ++n){
        for (double beta = 0; beta < M_PI * 2; beta += step, count += 4){
            double x = (R + r * cos(alpha)) * cos(beta);
            double y = (R + r * cos(alpha)) * sin(beta);
            double z = r * sin(alpha);
            ob->addpoint(x, y, z);
            x = (R + r * cos(alpha + step)) * cos(beta);
            y = (R + r * cos(alpha + step)) * sin(beta);
            z = r * sin(alpha + step);
            ob->addpoint(x, y, z);
            x = (R + r * cos(alpha + step)) * cos(beta + step);
            y = (R + r * cos(alpha + step)) * sin(beta + step);
            z = r * sin(alpha + step);
            ob->addpoint(x, y, z);
            x = (R + r * cos(alpha)) * cos(beta + step);
            y = (R + r * cos(alpha)) * sin(beta + step);
            z = r * sin(alpha);
            ob->addpoint(x, y, z);
            ob->addfacet(count + 3, count + 2, count + 1, count + 0);
        }
    }
    /*for (int i = 0; i < count * 2 - 3; i += 2){
        ob->addfacet(i + 2, i + 3, i + 1, i + 0);
    }*/
    return *ob;
}

Object getthird(){
    Object *ob = new Object;
    double r = a, h = b;
    int count = 0;
    for (double al = 0; al < 2 * M_PI; al += step, ++count){
        ob->addpoint(r * sin(al), r * cos(al), - h / 2);
        ob->addpoint(r * sin(al), r * cos(al), h / 2);
    }
    for (double al = 0; al < 2 * M_PI; al += step){
        ob->addpoint(2 * r * sin(al), 2 * r * cos(al), - h / 2);
    }
    ob->addpoint(r * sin(0), r * cos(0), - h / 2);
    ob->addpoint(r * sin(0), r * cos(0), h / 2);
    vector<int> top, bot, side, bot2;
    for (int i = 0; i < count; ++i){
        bot.push_back(2 *  count + i);
        bot2.push_back(3 * count - 1 - i);
        top.push_back(2 * count - 2 * i - 1);
        if (i == count - 1){
            continue;
        }
        side.clear();
        side.push_back(2 * i + 0);
        side.push_back(2 * i + 1);
        side.push_back(2 * i + 3);
        side.push_back(2 * i + 2);
        ob->addfacet(side);
    }
    side.clear();
    side.push_back(2 * count - 2);
    side.push_back(2 * count - 1);
    side.push_back(1);
    side.push_back(0);
    ob->addfacet(side);
    ob->addfacet(bot);
    ob->addfacet(bot2);
    ob->addfacet(top);
    return *ob;
}

Object (*getObject)() = getfirst;

Canvas canv;

void MainWindow::paintEvent(QPaintEvent *){
    maxx = width() - 300;
    maxy = height() - 35;
    Point center((minx + maxx) / 2, (miny + maxy) / 2, 0);
    Matrix matrix = Matrix().move(center) *
                    Matrix().rotateX(beta) *
                    Matrix().rotateY(alpha);

    Object ob = getObject();
    ob.setAmbient(ar, ag, ab);
    ob.setDiffuse(dr, dg, db);
    ob.setSpecular(sr, sg, sb, specpow);

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
    this->close();
}

void MainWindow::on_comboBox_currentIndexChanged(int index){
    if (index == 0){//cylinder
        getObject = getfirst;
        a = 100;
        b = 100;
        step = 0.07;
        dr = 0.3; dg = 0.3; db = 0.3;
        ar = 0.1; ag = 0.1; ab = 0.2;
        sr = 0.5; sg = 0.5; sb = 0.0;
        alpha = -3.6;
        beta = -2.1;
    }
    if (index == 1){//tor
        getObject = getsecond;
        a = 100;
        b = 50;
        step = 0.07;
        dr = 0.3; dg = 0.3; db = 0.3;
        ar = 0.1; ag = 0.1; ab = 0.2;
        sr = 0.5; sg = 0.5; sb = 0.0;
        alpha = -2.8;
        beta = -2.6;
    }
    if (index == 2){//hat
        getObject = getthird;
        a = 100;
        b = 120;
        step = 0.07;
        dr = 0.3; dg = 0.3; db = 0.3;
        ar = 0.1; ag = 0.1; ab = 0.2;
        sr = 0.5; sg = 0.5; sb = 0.0;
        alpha = 7.54;
        beta = -1.3;
    }
    update();
}

void MainWindow::on_doubleSpinBox_valueChanged(double arg1){
    a = arg1;
    update();
}

void MainWindow::on_doubleSpinBox_2_valueChanged(double arg1){
    b = arg1;
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

void MainWindow::on_doubleSpinBoxDR_valueChanged(double arg1){
    dr = arg1;
    update();
}

void MainWindow::on_doubleSpinBoxDG_valueChanged(double arg1){
    dg = arg1;
    update();
}

void MainWindow::on_doubleSpinBoxDB_valueChanged(double arg1){
    db = arg1;
    update();
}

void MainWindow::on_doubleSpinBoxAR_valueChanged(double arg1){
    ar = arg1;
    update();
}

void MainWindow::on_doubleSpinBoxAG_valueChanged(double arg1){
    ag = arg1;
    update();
}

void MainWindow::on_doubleSpinBoxAB_valueChanged(double arg1){
    ab = arg1;
    update();
}

void MainWindow::on_doubleSpinBoxSR_valueChanged(double arg1){
    sr = arg1;
    update();
}

void MainWindow::on_doubleSpinBoxSG_valueChanged(double arg1){
    sg = arg1;
    update();
}

void MainWindow::on_doubleSpinBoxSB_valueChanged(double arg1){
    sb = arg1;
    update();
}
