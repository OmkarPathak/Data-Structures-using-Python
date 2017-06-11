# Author: OMKAR PATHAk

from Arrays import Array

def rotation(rotateBy, myArray):
    for i in range(0, rotateBy):
        rotateOne(myArray)
    return myArray

def rotateOne(myArray):
    for i in range(len(myArray) - 1):
        myArray[i], myArray[i + 1] = myArray[i + 1], myArray[i]


if __name__ == '__main__':
    myArray = Array(10)
    for i in range(len(myArray)):
        myArray.insert(i, i)
    print('Before Rotation:',myArray)
    print('After Rotation:',rotation(3, myArray))

    # OUTPUT:
    # Before Rotation: 0 1 2 3 4 5 6 7 8 9
    # After Rotation: 3 4 5 6 7 8 9 0 1 2
