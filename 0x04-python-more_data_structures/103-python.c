#include <stdio.h>
#include <Python.h>
#include <pytime.h>

/**
 * print_python_list - prints a list of integers
 * @p: list of integers
 * Return: nothing
*/

void print_python_list(PyObject *p)
{
	Py_ssize_t i;
	PyObject *o;

	for (i = 0; i < PyList_Size(p); i++)
	{
		o = PyList_GetItem(p, i);
		PyObject *str_obj = PyUnicode_AsUTF8String(o);
		if (str_obj == NULL)
		{
			PyErr_Print();
			return;
		}
		char *str = PyBytes_AsString(str_obj);
		if (str == NULL)
		{
			PyErr_Print();
			Py_DECREF(str_obj);
			return;
		}
		printf("%s\n", str);
		Py_DECREF(str_obj);
	}
}
