# Author: OMKAR PATHAK

# Given an array A[] of n numbers and another number x, determines whether or not there exist two elements
# in S whose sum is exactly x.

def checkSum(array, sum):
    # sort the array in descending order
    array = quickSort(array)

    leftIndex = 0
    rightIndex = len(array) - 1

    while leftIndex < rightIndex:
        if (array[leftIndex] + array[rightIndex] ==  sum):
            return array[leftIndex], array[rightIndex]
        elif(array[leftIndex] + array[rightIndex] < sum):
            leftIndex += 1
        else:
            rightIndex += 1

    return False, False

def quickSort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return quickSort(left) + middle + quickSort(right)

if __name__ == '__main__':
    myArray = [10, 20, 30, 40, 50]
    sum = 80

    number1, number2 = checkSum(myArray, sum)
    if(number1 and number2):
        print('Array has elements:', number1, 'and', number2, 'with sum:', sum)
    else:
        print('Array doesn\'t has elements with the sum:', sum)
