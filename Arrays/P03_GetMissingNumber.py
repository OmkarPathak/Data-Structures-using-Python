# Author: OMKAR PATHAk

from Arrays import Array

def findMissing(myArray, n):
    n = n - 1
    totalSum = (n * (n + 1)) // 2
    for i in range(0, n):
        totalSum -= myArray[i]

    return totalSum

if __name__ == '__main__':
    myArray = Array(10)
    for i in range(len(myArray)):
        myArray.insert(i, i)
    myArray.delete(4, 4)
    print('Original Array:',myArray)
    print('Missing Element:', findMissing(myArray, len(myArray)))

    # OUTPUT:
    # Original Array: 0 1 2 3 5 6 7 8 9 0
    # Missing Element: 4
