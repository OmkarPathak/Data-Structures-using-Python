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
    if number == 1 or number == 0:
        return number
    else:
        return (fibonacciRec(number - 1) + fibonacciRec(number - 2))

# improved recursive fibonacci function
def fib_memoization(n, lookup): 
    if n == 0 or n == 1 : 
        lookup[n] = n 
    if lookup[n] is None: 
        lookup[n] = fib(n-1 , lookup)  + fib(n-2 , lookup)  
    return lookup[n]


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
    
    startTime = time.time()
    lookup=[None]*(101) 
    result = fib_memoization(userInput,lookup)
    stopTime = time.time()
    print('Time:', (stopTime - startTime), 'Result:', result)
