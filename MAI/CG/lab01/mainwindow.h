#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();
    void paintEvent(QPaintEvent *);
    void mousePressEvent(QMouseEvent *);
    void mouseMoveEvent(QMouseEvent *);

    double alpha, beta;
private slots:

    void on_spinBoxA_valueChanged(int arg1);

    void on_spinBoxB_valueChanged(int arg1);

    void on_spinBoxC_valueChanged(int arg1);

    void on_doubleSpinBox_valueChanged(double arg1);

    void on_doubleSpinBox_2_valueChanged(double arg1);

    void on_doubleSpinBox_3_valueChanged(double arg1);

    void on_doubleSpinBox_4_valueChanged(double arg1);

    void on_radioButton_clicked();

    void on_radioButton_2_clicked();

    void on_CloseButton_clicked();

private:
    Ui::MainWindow *ui;
};

#endif // MAINWINDOW_H
