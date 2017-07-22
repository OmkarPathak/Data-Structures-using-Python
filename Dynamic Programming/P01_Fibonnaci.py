# Author: OMKAR PATHAK

# recursive fibonacci solution has a time complexity of O(2 ^ n).
# To reduce this we can use dynamic programming. Dictionary data structure is used to drastically reduce
# the time complexity to O(n)

import time

# improved fibonacci function
def fibonacci(number):
    if myList[number] == None:
        myList[number] = fibonacci(number - 1) + fibonacci(number - 2)
    return myList[number]

# traditional recursive fibonacci function
def fibonacciRec(number):
    if number <= 1:
        return number
    else:
        return (fibonacciRec(number - 1) + fibonacciRec(number - 2))

if __name__ == '__main__':
    userInput = int(input('Enter the number: '))

    myList = [None for _ in range(userInput + 1)]

    # base cases
    myList[0] = 0
    myList[1] = 1

    startTime = time.time()
    result = fibonacci(userInput)
    stopTime = time.time()
    print('Time:', (stopTime - startTime), 'Result:', result)

    startTime = time.time()
    result = fibonacciRec(userInput)
    stopTime = time.time()
    print('Time:', (stopTime - startTime), 'Result:', result)
