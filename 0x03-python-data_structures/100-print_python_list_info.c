#include <Python.h>
/**
 * print_python_list_info - Print information about a Python list.
 * @p: A pointer to a PyObject representing a Python list.
 *
 * This function prints information about a Python list, including its size
 * (number of elements) and the allocated memory size. It also iterates
 * through the list elements and prints the type of each element.
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, alloc;
	int i;

	if (!PyList_Check(p)) /* Check if 'p' is a Python list */
	{
		fprintf(stderr, "Invalid Python list\n");
		return;
	}

	/* Get the size (number of elements) of the list */
	size = PyList_Size(p);

	/* Get the allocated memory size */
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	for (i = 0; i < size; i++) /* Iterate through the list elements */
	{
		PyObject *element = PyList_GetItem(p, i); /* Get the i-th element */

		/* Check if element retrieval was successful */
		if (element != NULL)
		{
			printf("Element %d: %s\n", i, Py_TYPE(element)->tp_name);
		}
		else
		{
			fprintf(stderr, "Failed to retrieve element %d\n", i);
		}
	}
}
