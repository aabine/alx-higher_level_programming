#include <stdio.h>
#include "sort.h"

void bubble_sort(int *array, size_t size)
{
    size_t i;
    size_t j;
    int temp;
    int swapped;

    if (size <= 1)
        return;


    for (i = 0; i < size - 1; i++)
    {
        swapped = 0;

        for (j = 0; j < size - i - 1; j++)
        {
            if (array[j] > array[j + 1])
            {
                temp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = temp;

                swapped = 1;

                print_array(array, size);
            }
        }

        if (!swapped)
            break;
    }
}
