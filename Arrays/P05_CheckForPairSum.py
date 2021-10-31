# Author: OMKAR PATHAK

# Given an array A[] of n numbers and another number x, determines whether or not there exist two elements
# in S whose total is exactly x.

def check_sum(array, sum):
    # sort the array in ascending order
    # new changes : made use of Python's inbuilt Merge Sort method
    # Reason for such change : Worst case Time complexity of Quick Sort is O(n^2) whereas Worst Case Complexity of Merge Sort is O(nlog(n))
    array = sorted(array)

    left_index = 0
    right_index = len(array) - 1

    while left_index < right_index:
        if (array[left_index] + array[right_index] == sum):
            return array[left_index], array[right_index]
        elif (array[left_index] + array[right_index] < sum):
            left_index += 1
        else:
            right_index += 1

    return False, False


##def quickSort(array):
##    if len(array) <= 1:
##        return array
##    pivot = array[len(array) // 2]
##    left = [x for x in array if x < pivot]
##    middle = [x for x in array if x == pivot]
##    right = [x for x in array if x > pivot]
##    return quickSort(left) + middle + quickSort(right)

if __name__ == '__main__':
    my_array = [10, 20, 30, 40, 50]
    total = 80

    number1, number2 = check_sum(my_array, total)
    if number1 and number2:
        print('Array has elements:', number1, 'and', number2, 'with total:', total)
    else:
        print('Array doesn\'t have elements with the total:', total)
