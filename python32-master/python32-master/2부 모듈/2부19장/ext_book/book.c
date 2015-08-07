#include "Python.h"

static PyObject *
book_print(PyObject *self, PyObject *args)
{
    const char* str="module name is book";
    
    return Py_BuildValue("s", str);
}

static PyMethodDef BookMethods[] = {
	 {"print", book_print, METH_VARARGS,
     "print book module information."},
     {NULL, NULL, 0, NULL}    //�迭�� ���� ��Ÿ���ϴ�.
};

static struct PyModuleDef bookmodule = {
   PyModuleDef_HEAD_INIT,
   "book.page",               // ��� �̸�
   "It is test module.", 
   -1,BookMethods
};

PyMODINIT_FUNC
PyInit_book(void)
{
    return PyModule_Create(&bookmodule);
}

PyMODINIT_FUNC
PyInit_page(void)
{
    return PyModule_Create(&bookmodule);
}
