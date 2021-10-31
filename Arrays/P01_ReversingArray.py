# Author: OMKAR PATHAK

import Arrays


def reversing_an_array(start, end, my_array):
    while (start < end):
        my_array[start], my_array[end - 1] = my_array[end - 1], my_array[start]
        start += 1
        end -= 1


if __name__ == '__main__':
    my_array = Arrays.Array(10)
    my_array.insert(2, 2)
    my_array.insert(1, 3)
    my_array.insert(3, 1)
    print('Array before Reversing:', my_array)
    reversing_an_array(0, len(my_array), my_array)
    print('Array after Reversing:', my_array)
