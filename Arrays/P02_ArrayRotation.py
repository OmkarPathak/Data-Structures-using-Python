# Author: OMKAR PATHAk

from Arrays import Array


def rotation(rotate_by, my_array):
    for i in range(0, rotate_by):
        rotate_one(my_array)
    return my_array


def rotate_one(my_array):
    for i in range(len(my_array) - 1):
        my_array[i], my_array[i + 1] = my_array[i + 1], my_array[i]


if __name__ == '__main__':
    my_array = Array(10)
    for i in range(len(my_array)):
        my_array.insert(i, i)
    print('Before Rotation:', my_array)
    print('After Rotation:', rotation(3, my_array))

    # OUTPUT:
    # Before Rotation: 0 1 2 3 4 5 6 7 8 9
    # After Rotation: 3 4 5 6 7 8 9 0 1 2
