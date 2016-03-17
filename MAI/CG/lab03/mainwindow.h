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

private slots:
    void on_pushButton_clicked();

    void on_comboBox_currentIndexChanged(int index);

    void on_doubleSpinBox_valueChanged(double arg1);

    void on_doubleSpinBox_2_valueChanged(double arg1);

    void on_doubleSpinBox_3_valueChanged(double arg1);

    void on_doubleSpinBox_4_valueChanged(double arg1);

    void on_doubleSpinBox_5_valueChanged(double arg1);

    void on_doubleSpinBoxDR_valueChanged(double arg1);

    void on_doubleSpinBoxDG_valueChanged(double arg1);

    void on_doubleSpinBoxDB_valueChanged(double arg1);

    void on_doubleSpinBoxAR_valueChanged(double arg1);

    void on_doubleSpinBoxAG_valueChanged(double arg1);

    void on_doubleSpinBoxAB_valueChanged(double arg1);

    void on_doubleSpinBoxSR_valueChanged(double arg1);

    void on_doubleSpinBoxSG_valueChanged(double arg1);

    void on_doubleSpinBoxSB_valueChanged(double arg1);

private:
    Ui::MainWindow *ui;
    double alpha, beta;
};

#endif // MAINWINDOW_H
