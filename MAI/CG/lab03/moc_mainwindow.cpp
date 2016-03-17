/****************************************************************************
** Meta object code from reading C++ file 'mainwindow.h'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.6)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "mainwindow.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'mainwindow.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.6. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_MainWindow[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
      16,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: signature, parameters, type, tag, flags
      12,   11,   11,   11, 0x08,
      42,   36,   11,   11, 0x08,
      84,   79,   11,   11, 0x08,
     122,   79,   11,   11, 0x08,
     162,   79,   11,   11, 0x08,
     202,   79,   11,   11, 0x08,
     242,   79,   11,   11, 0x08,
     282,   79,   11,   11, 0x08,
     322,   79,   11,   11, 0x08,
     362,   79,   11,   11, 0x08,
     402,   79,   11,   11, 0x08,
     442,   79,   11,   11, 0x08,
     482,   79,   11,   11, 0x08,
     522,   79,   11,   11, 0x08,
     562,   79,   11,   11, 0x08,
     602,   79,   11,   11, 0x08,

       0        // eod
};

static const char qt_meta_stringdata_MainWindow[] = {
    "MainWindow\0\0on_pushButton_clicked()\0"
    "index\0on_comboBox_currentIndexChanged(int)\0"
    "arg1\0on_doubleSpinBox_valueChanged(double)\0"
    "on_doubleSpinBox_2_valueChanged(double)\0"
    "on_doubleSpinBox_3_valueChanged(double)\0"
    "on_doubleSpinBox_4_valueChanged(double)\0"
    "on_doubleSpinBox_5_valueChanged(double)\0"
    "on_doubleSpinBoxDR_valueChanged(double)\0"
    "on_doubleSpinBoxDG_valueChanged(double)\0"
    "on_doubleSpinBoxDB_valueChanged(double)\0"
    "on_doubleSpinBoxAR_valueChanged(double)\0"
    "on_doubleSpinBoxAG_valueChanged(double)\0"
    "on_doubleSpinBoxAB_valueChanged(double)\0"
    "on_doubleSpinBoxSR_valueChanged(double)\0"
    "on_doubleSpinBoxSG_valueChanged(double)\0"
    "on_doubleSpinBoxSB_valueChanged(double)\0"
};

void MainWindow::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        MainWindow *_t = static_cast<MainWindow *>(_o);
        switch (_id) {
        case 0: _t->on_pushButton_clicked(); break;
        case 1: _t->on_comboBox_currentIndexChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 2: _t->on_doubleSpinBox_valueChanged((*reinterpret_cast< double(*)>(_a[1]))); break;
        case 3: _t->on_doubleSpinBox_2_valueChanged((*reinterpret_cast< double(*)>(_a[1]))); break;
        case 4: _t->on_doubleSpinBox_3_valueChanged((*reinterpret_cast< double(*)>(_a[1]))); break;
        case 5: _t->on_doubleSpinBox_4_valueChanged((*reinterpret_cast< double(*)>(_a[1]))); break;
        case 6: _t->on_doubleSpinBox_5_valueChanged((*reinterpret_cast< double(*)>(_a[1]))); break;
        case 7: _t->on_doubleSpinBoxDR_valueChanged((*reinterpret_cast< double(*)>(_a[1]))); break;
        case 8: _t->on_doubleSpinBoxDG_valueChanged((*reinterpret_cast< double(*)>(_a[1]))); break;
        case 9: _t->on_doubleSpinBoxDB_valueChanged((*reinterpret_cast< double(*)>(_a[1]))); break;
        case 10: _t->on_doubleSpinBoxAR_valueChanged((*reinterpret_cast< double(*)>(_a[1]))); break;
        case 11: _t->on_doubleSpinBoxAG_valueChanged((*reinterpret_cast< double(*)>(_a[1]))); break;
        case 12: _t->on_doubleSpinBoxAB_valueChanged((*reinterpret_cast< double(*)>(_a[1]))); break;
        case 13: _t->on_doubleSpinBoxSR_valueChanged((*reinterpret_cast< double(*)>(_a[1]))); break;
        case 14: _t->on_doubleSpinBoxSG_valueChanged((*reinterpret_cast< double(*)>(_a[1]))); break;
        case 15: _t->on_doubleSpinBoxSB_valueChanged((*reinterpret_cast< double(*)>(_a[1]))); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData MainWindow::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject MainWindow::staticMetaObject = {
    { &QMainWindow::staticMetaObject, qt_meta_stringdata_MainWindow,
      qt_meta_data_MainWindow, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &MainWindow::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *MainWindow::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *MainWindow::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_MainWindow))
        return static_cast<void*>(const_cast< MainWindow*>(this));
    return QMainWindow::qt_metacast(_clname);
}

int MainWindow::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QMainWindow::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 16)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 16;
    }
    return _id;
}
QT_END_MOC_NAMESPACE
