/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 4.8.6
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QComboBox>
#include <QtGui/QDoubleSpinBox>
#include <QtGui/QGridLayout>
#include <QtGui/QHBoxLayout>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QMainWindow>
#include <QtGui/QMenuBar>
#include <QtGui/QPushButton>
#include <QtGui/QSpacerItem>
#include <QtGui/QStatusBar>
#include <QtGui/QToolBar>
#include <QtGui/QVBoxLayout>
#include <QtGui/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralWidget;
    QGridLayout *gridLayout;
    QSpacerItem *horizontalSpacer;
    QVBoxLayout *verticalLayout_6;
    QHBoxLayout *horizontalLayout;
    QLabel *label_2;
    QDoubleSpinBox *doubleSpinBox;
    QLabel *label;
    QDoubleSpinBox *doubleSpinBox_2;
    QHBoxLayout *horizontalLayout_3;
    QVBoxLayout *verticalLayout_5;
    QHBoxLayout *horizontalLayout_2;
    QLabel *label_5;
    QDoubleSpinBox *doubleSpinBox_5;
    QVBoxLayout *verticalLayout_4;
    QLabel *label_7;
    QLabel *label_8;
    QLabel *label_9;
    QVBoxLayout *verticalLayout_3;
    QLabel *label_3;
    QDoubleSpinBox *doubleSpinBoxDR;
    QDoubleSpinBox *doubleSpinBoxAR;
    QDoubleSpinBox *doubleSpinBoxSR;
    QVBoxLayout *verticalLayout_2;
    QLabel *label_4;
    QDoubleSpinBox *doubleSpinBoxDG;
    QDoubleSpinBox *doubleSpinBoxAG;
    QDoubleSpinBox *doubleSpinBoxSG;
    QVBoxLayout *verticalLayout;
    QLabel *label_6;
    QDoubleSpinBox *doubleSpinBoxDB;
    QDoubleSpinBox *doubleSpinBoxAB;
    QDoubleSpinBox *doubleSpinBoxSB;
    QHBoxLayout *horizontalLayout_7;
    QPushButton *pushButton;
    QComboBox *comboBox;
    QSpacerItem *verticalSpacer;
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(602, 389);
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        gridLayout = new QGridLayout(centralWidget);
        gridLayout->setSpacing(6);
        gridLayout->setContentsMargins(11, 11, 11, 11);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        horizontalSpacer = new QSpacerItem(232, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer, 0, 0, 1, 1);

        verticalLayout_6 = new QVBoxLayout();
        verticalLayout_6->setSpacing(6);
        verticalLayout_6->setObjectName(QString::fromUtf8("verticalLayout_6"));
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setSpacing(6);
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        label_2 = new QLabel(centralWidget);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        horizontalLayout->addWidget(label_2);

        doubleSpinBox = new QDoubleSpinBox(centralWidget);
        doubleSpinBox->setObjectName(QString::fromUtf8("doubleSpinBox"));
        doubleSpinBox->setDecimals(0);
        doubleSpinBox->setMinimum(1);
        doubleSpinBox->setMaximum(1000);
        doubleSpinBox->setSingleStep(5);
        doubleSpinBox->setValue(100);

        horizontalLayout->addWidget(doubleSpinBox);

        label = new QLabel(centralWidget);
        label->setObjectName(QString::fromUtf8("label"));

        horizontalLayout->addWidget(label);

        doubleSpinBox_2 = new QDoubleSpinBox(centralWidget);
        doubleSpinBox_2->setObjectName(QString::fromUtf8("doubleSpinBox_2"));
        doubleSpinBox_2->setDecimals(0);
        doubleSpinBox_2->setMinimum(1);
        doubleSpinBox_2->setMaximum(1000);
        doubleSpinBox_2->setSingleStep(5);
        doubleSpinBox_2->setValue(100);

        horizontalLayout->addWidget(doubleSpinBox_2);


        verticalLayout_6->addLayout(horizontalLayout);

        horizontalLayout_3 = new QHBoxLayout();
        horizontalLayout_3->setSpacing(6);
        horizontalLayout_3->setObjectName(QString::fromUtf8("horizontalLayout_3"));
        verticalLayout_5 = new QVBoxLayout();
        verticalLayout_5->setSpacing(6);
        verticalLayout_5->setObjectName(QString::fromUtf8("verticalLayout_5"));
        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setSpacing(6);
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        label_5 = new QLabel(centralWidget);
        label_5->setObjectName(QString::fromUtf8("label_5"));

        horizontalLayout_2->addWidget(label_5);

        doubleSpinBox_5 = new QDoubleSpinBox(centralWidget);
        doubleSpinBox_5->setObjectName(QString::fromUtf8("doubleSpinBox_5"));
        doubleSpinBox_5->setDecimals(3);
        doubleSpinBox_5->setMinimum(0.05);
        doubleSpinBox_5->setMaximum(1);
        doubleSpinBox_5->setSingleStep(0.01);

        horizontalLayout_2->addWidget(doubleSpinBox_5);


        verticalLayout_5->addLayout(horizontalLayout_2);

        verticalLayout_4 = new QVBoxLayout();
        verticalLayout_4->setSpacing(6);
        verticalLayout_4->setObjectName(QString::fromUtf8("verticalLayout_4"));
        label_7 = new QLabel(centralWidget);
        label_7->setObjectName(QString::fromUtf8("label_7"));

        verticalLayout_4->addWidget(label_7);

        label_8 = new QLabel(centralWidget);
        label_8->setObjectName(QString::fromUtf8("label_8"));

        verticalLayout_4->addWidget(label_8);

        label_9 = new QLabel(centralWidget);
        label_9->setObjectName(QString::fromUtf8("label_9"));

        verticalLayout_4->addWidget(label_9);


        verticalLayout_5->addLayout(verticalLayout_4);


        horizontalLayout_3->addLayout(verticalLayout_5);

        verticalLayout_3 = new QVBoxLayout();
        verticalLayout_3->setSpacing(6);
        verticalLayout_3->setObjectName(QString::fromUtf8("verticalLayout_3"));
        label_3 = new QLabel(centralWidget);
        label_3->setObjectName(QString::fromUtf8("label_3"));

        verticalLayout_3->addWidget(label_3);

        doubleSpinBoxDR = new QDoubleSpinBox(centralWidget);
        doubleSpinBoxDR->setObjectName(QString::fromUtf8("doubleSpinBoxDR"));
        doubleSpinBoxDR->setDecimals(1);
        doubleSpinBoxDR->setMaximum(1);
        doubleSpinBoxDR->setSingleStep(0.1);
        doubleSpinBoxDR->setValue(0.3);

        verticalLayout_3->addWidget(doubleSpinBoxDR);

        doubleSpinBoxAR = new QDoubleSpinBox(centralWidget);
        doubleSpinBoxAR->setObjectName(QString::fromUtf8("doubleSpinBoxAR"));
        doubleSpinBoxAR->setDecimals(1);
        doubleSpinBoxAR->setMaximum(1);
        doubleSpinBoxAR->setSingleStep(0.1);
        doubleSpinBoxAR->setValue(0.1);

        verticalLayout_3->addWidget(doubleSpinBoxAR);

        doubleSpinBoxSR = new QDoubleSpinBox(centralWidget);
        doubleSpinBoxSR->setObjectName(QString::fromUtf8("doubleSpinBoxSR"));
        doubleSpinBoxSR->setDecimals(1);
        doubleSpinBoxSR->setMaximum(1);
        doubleSpinBoxSR->setSingleStep(0.1);
        doubleSpinBoxSR->setValue(0.5);

        verticalLayout_3->addWidget(doubleSpinBoxSR);


        horizontalLayout_3->addLayout(verticalLayout_3);

        verticalLayout_2 = new QVBoxLayout();
        verticalLayout_2->setSpacing(6);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        label_4 = new QLabel(centralWidget);
        label_4->setObjectName(QString::fromUtf8("label_4"));

        verticalLayout_2->addWidget(label_4);

        doubleSpinBoxDG = new QDoubleSpinBox(centralWidget);
        doubleSpinBoxDG->setObjectName(QString::fromUtf8("doubleSpinBoxDG"));
        doubleSpinBoxDG->setDecimals(1);
        doubleSpinBoxDG->setMaximum(1);
        doubleSpinBoxDG->setSingleStep(0.1);
        doubleSpinBoxDG->setValue(0.3);

        verticalLayout_2->addWidget(doubleSpinBoxDG);

        doubleSpinBoxAG = new QDoubleSpinBox(centralWidget);
        doubleSpinBoxAG->setObjectName(QString::fromUtf8("doubleSpinBoxAG"));
        doubleSpinBoxAG->setDecimals(1);
        doubleSpinBoxAG->setMaximum(1);
        doubleSpinBoxAG->setSingleStep(0.1);
        doubleSpinBoxAG->setValue(0.1);

        verticalLayout_2->addWidget(doubleSpinBoxAG);

        doubleSpinBoxSG = new QDoubleSpinBox(centralWidget);
        doubleSpinBoxSG->setObjectName(QString::fromUtf8("doubleSpinBoxSG"));
        doubleSpinBoxSG->setDecimals(1);
        doubleSpinBoxSG->setMaximum(1);
        doubleSpinBoxSG->setSingleStep(0.1);
        doubleSpinBoxSG->setValue(0.5);

        verticalLayout_2->addWidget(doubleSpinBoxSG);


        horizontalLayout_3->addLayout(verticalLayout_2);

        verticalLayout = new QVBoxLayout();
        verticalLayout->setSpacing(6);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        label_6 = new QLabel(centralWidget);
        label_6->setObjectName(QString::fromUtf8("label_6"));

        verticalLayout->addWidget(label_6);

        doubleSpinBoxDB = new QDoubleSpinBox(centralWidget);
        doubleSpinBoxDB->setObjectName(QString::fromUtf8("doubleSpinBoxDB"));
        doubleSpinBoxDB->setDecimals(1);
        doubleSpinBoxDB->setMaximum(1);
        doubleSpinBoxDB->setSingleStep(0.1);
        doubleSpinBoxDB->setValue(0.3);

        verticalLayout->addWidget(doubleSpinBoxDB);

        doubleSpinBoxAB = new QDoubleSpinBox(centralWidget);
        doubleSpinBoxAB->setObjectName(QString::fromUtf8("doubleSpinBoxAB"));
        doubleSpinBoxAB->setDecimals(1);
        doubleSpinBoxAB->setMaximum(1);
        doubleSpinBoxAB->setSingleStep(0.1);
        doubleSpinBoxAB->setValue(0.2);

        verticalLayout->addWidget(doubleSpinBoxAB);

        doubleSpinBoxSB = new QDoubleSpinBox(centralWidget);
        doubleSpinBoxSB->setObjectName(QString::fromUtf8("doubleSpinBoxSB"));
        doubleSpinBoxSB->setDecimals(1);
        doubleSpinBoxSB->setMaximum(1);
        doubleSpinBoxSB->setSingleStep(0.1);

        verticalLayout->addWidget(doubleSpinBoxSB);


        horizontalLayout_3->addLayout(verticalLayout);


        verticalLayout_6->addLayout(horizontalLayout_3);

        horizontalLayout_7 = new QHBoxLayout();
        horizontalLayout_7->setSpacing(6);
        horizontalLayout_7->setObjectName(QString::fromUtf8("horizontalLayout_7"));
        pushButton = new QPushButton(centralWidget);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));

        horizontalLayout_7->addWidget(pushButton);

        comboBox = new QComboBox(centralWidget);
        comboBox->setObjectName(QString::fromUtf8("comboBox"));

        horizontalLayout_7->addWidget(comboBox);


        verticalLayout_6->addLayout(horizontalLayout_7);


        gridLayout->addLayout(verticalLayout_6, 0, 1, 1, 1);

        verticalSpacer = new QSpacerItem(20, 62, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer, 1, 1, 1, 1);

        MainWindow->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName(QString::fromUtf8("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 602, 25));
        MainWindow->setMenuBar(menuBar);
        mainToolBar = new QToolBar(MainWindow);
        mainToolBar->setObjectName(QString::fromUtf8("mainToolBar"));
        MainWindow->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(MainWindow);
        statusBar->setObjectName(QString::fromUtf8("statusBar"));
        MainWindow->setStatusBar(statusBar);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", 0, QApplication::UnicodeUTF8));
        label_2->setText(QApplication::translate("MainWindow", "A:", 0, QApplication::UnicodeUTF8));
        label->setText(QApplication::translate("MainWindow", "B:", 0, QApplication::UnicodeUTF8));
        label_5->setText(QApplication::translate("MainWindow", "Step:", 0, QApplication::UnicodeUTF8));
        label_7->setText(QApplication::translate("MainWindow", "Diffuse:", 0, QApplication::UnicodeUTF8));
        label_8->setText(QApplication::translate("MainWindow", "Ambient:", 0, QApplication::UnicodeUTF8));
        label_9->setText(QApplication::translate("MainWindow", "Speculate:", 0, QApplication::UnicodeUTF8));
        label_3->setText(QApplication::translate("MainWindow", "Red", 0, QApplication::UnicodeUTF8));
        label_4->setText(QApplication::translate("MainWindow", "Green", 0, QApplication::UnicodeUTF8));
        label_6->setText(QApplication::translate("MainWindow", "Blue", 0, QApplication::UnicodeUTF8));
        pushButton->setText(QApplication::translate("MainWindow", "Exit", 0, QApplication::UnicodeUTF8));
        comboBox->clear();
        comboBox->insertItems(0, QStringList()
         << QApplication::translate("MainWindow", "Cylinder", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "Tor", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("MainWindow", "Hat", 0, QApplication::UnicodeUTF8)
        );
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
