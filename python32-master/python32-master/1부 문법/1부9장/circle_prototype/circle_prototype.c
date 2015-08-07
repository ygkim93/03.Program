#include <python.h>

typedef struct {
   PyObject_HEAD
} circle_CircleObject;

static PyTypeObject circle_CircleType = {
    PyObject_HEAD_INIT(NULL)
    "circle.Circle",             /* tp_name */
    sizeof(circle_CircleObject), /* tp_basicsize */
    0,                         /* tp_itemsize */
    0,                         /* tp_dealloc */
    0,                         /* tp_print */
    0,                         /* tp_getattr */
    0,                         /* tp_setattr */
    0,                         /* tp_reserved */
    0,                         /* tp_repr */
    0,                         /* tp_as_number */
    0,                         /* tp_as_sequence */
    0,                         /* tp_as_mapping */
    0,                         /* tp_hash  */
    0,                         /* tp_call */
    0,                         /* tp_str */
    0,                         /* tp_getattro */
    0,                         /* tp_setattro */
    0,                         /* tp_as_buffer */
    Py_TPFLAGS_DEFAULT,        /* tp_flags */
    "Circle objects",           /* tp_doc */
};

static PyModuleDef circlemodule = {
    PyModuleDef_HEAD_INIT,
    "circle",
    "Example module that creates an extension type.",
    -1,
    NULL, NULL, NULL, NULL, NULL
};

PyMODINIT_FUNC
PyInit_circle(void)
{
    PyObject* m;
    circle_CircleType.tp_new = PyType_GenericNew;
    if (PyType_Ready(&circle_CircleType) < 0)
        return NULL;

    m = PyModule_Create(&circlemodule);
    if (m == NULL)
        return NULL;

    Py_INCREF(&circle_CircleType);
    PyModule_AddObject(m, "Circle", (PyObject *)&circle_CircleType);
    return m;
} 
