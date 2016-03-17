#-------------------------------------------------
#
# Project created by QtCreator 2015-09-22T09:54:48
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = lab0201
TEMPLATE = app


SOURCES += main.cpp\
        mainwindow.cpp \
    point.cpp \
    matrix.cpp \
    object.cpp \
    canvas.cpp

HEADERS  += mainwindow.h \
    object.h \
    point.h \
    matrix.h \
    canvas.h

FORMS    += mainwindow.ui
