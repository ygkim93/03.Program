#include "Python.h"

static PyObject *
page_print(PyObject *self, PyObject *args)
{
    const char* str="module name is page";
    
    return Py_BuildValue("s", str);
}

static PyMethodDef PageMethods[] = {
	 {"print", page_print, METH_VARARGS,
     "print page module information."},
     {NULL, NULL, 0, NULL}    //�迭�� ���� ��Ÿ���ϴ�.
};

static struct PyModuleDef pagemodule = {
   PyModuleDef_HEAD_INIT,
   "page",               // ��� �̸�
   "It is test module.", 
   -1,PageMethods
};

PyMODINIT_FUNC
PyInit_page(void)
{
    return PyModule_Create(&pagemodule);
}
