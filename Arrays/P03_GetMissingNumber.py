# Author: OMKAR PATHAk

from Arrays import Array


def find_missing(my_array, n):
    n = n - 1
    total_sum = (n * (n + 1)) // 2
    for i in range(0, n):
        total_sum -= my_array[i]

    return total_sum


if __name__ == '__main__':
    my_array = Array(10)
    for i in range(len(my_array)):
        my_array.insert(i, i)
    my_array.delete(4, 4)
    print('Original Array:', my_array)
    print('Missing Element:', find_missing(my_array, len(my_array)))

    # OUTPUT:
    # Original Array: 0 1 2 3 5 6 7 8 9 0
    # Missing Element: 4
