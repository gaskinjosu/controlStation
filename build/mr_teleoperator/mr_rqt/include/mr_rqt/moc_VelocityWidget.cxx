/****************************************************************************
** Meta object code from reading C++ file 'VelocityWidget.h'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.7)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../../../../../src/mr_teleoperator/mr_rqt/include/mr_rqt/VelocityWidget.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'VelocityWidget.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.7. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_mr_rqt__VelocityWidget[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
       2,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       1,       // signalCount

 // signals: signature, parameters, type, tag, flags
      24,   23,   23,   23, 0x05,

 // slots: signature, parameters, type, tag, flags
      39,   23,   23,   23, 0x0a,

       0        // eod
};

static const char qt_meta_stringdata_mr_rqt__VelocityWidget[] = {
    "mr_rqt::VelocityWidget\0\0redrawSignal()\0"
    "redraw()\0"
};

void mr_rqt::VelocityWidget::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        VelocityWidget *_t = static_cast<VelocityWidget *>(_o);
        switch (_id) {
        case 0: _t->redrawSignal(); break;
        case 1: _t->redraw(); break;
        default: ;
        }
    }
    Q_UNUSED(_a);
}

const QMetaObjectExtraData mr_rqt::VelocityWidget::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject mr_rqt::VelocityWidget::staticMetaObject = {
    { &QWidget::staticMetaObject, qt_meta_stringdata_mr_rqt__VelocityWidget,
      qt_meta_data_mr_rqt__VelocityWidget, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &mr_rqt::VelocityWidget::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *mr_rqt::VelocityWidget::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *mr_rqt::VelocityWidget::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_mr_rqt__VelocityWidget))
        return static_cast<void*>(const_cast< VelocityWidget*>(this));
    return QWidget::qt_metacast(_clname);
}

int mr_rqt::VelocityWidget::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QWidget::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 2)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 2;
    }
    return _id;
}

// SIGNAL 0
void mr_rqt::VelocityWidget::redrawSignal()
{
    QMetaObject::activate(this, &staticMetaObject, 0, 0);
}
QT_END_MOC_NAMESPACE
