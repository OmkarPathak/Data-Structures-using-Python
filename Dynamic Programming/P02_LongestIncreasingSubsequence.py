# Author:  OMKAR PATHAK

# The Longest Increasing Subsequence (LIS) problem is to find the length of the longest subsequence of a
# given sequence such that all elements of the subsequence are sorted in increasing order. For example,
# the length of LIS for {10, 22, 9, 33, 21, 50, 41, 60, 80} is 6 and LIS is {10, 22, 33, 50, 60, 80}.

def longest_increaing_subsequence(myList):
    # Initialize list with some value
    lis = [1] * len(myList)
    # list for storing the elements in an lis
    elements = [0] * len(myList)

    # Compute optimized LIS values in bottom up manner
    for i in range (1 , len(myList)):
        for j in range(0 , i):
            if myList[i] > myList[j] and lis[i]< lis[j] + 1:
                lis[i] = lis[j]+1
                elements[i] = j

    idx = 0

    # find the maximum of the whole list and get its index in idx
    maximum = max(lis)              # this will give us the count of longest increasing subsequence
    idx = lis.index(maximum)

    # for printing the elements later
    seq = [myList[idx]]
    while idx != elements[idx]:
        idx = elements[idx]
        seq.append(myList[idx])

    return (maximum, reversed(seq))

# define elements in an array
myList = [10, 22, 9, 33, 21, 50, 41, 60]
ans = longest_increaing_subsequence(myList)
print ('Length of lis is', ans[0])
print ('The longest sequence is', ', '.join(str(x) for x in ans[1]))

# OUTPUT:
# Length of lis is 5
# The longest sequence is 10, 22, 33, 50, 60
