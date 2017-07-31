# Author: OMKAR PATHAK

# this program will illustrate an example for finding the longest CONTINUOUS ODD subsequence

# INPUT: [2, 6, 8, 3, 9, 1, 5, 6, 1, 3, 5, 7, 7, 1, 2, 3, 4, 5]
# OUTPUT: [1, 3, 5, 7, 7, 1] 6

# in short we have to find the elements and length of the longest continuous odd subsequence

def longest_continuous_odd_subsequence(array):
    final_list = []
    temp_list = []
    for i in array:
        # we want to find whether the element is odd
        if i%2 == 0:
            # if element is even and our temp_list is not empty then only append it to out result list
            if temp_list != []:
                final_list.append(temp_list)
            temp_list = []
        else:
            # if element is odd, append it to our temp_list
            temp_list.append(i)

    # if temp_list is not empty at the last iteration, add it to the final_list
    if temp_list != []:
        final_list.append(temp_list)

    # print the maximum list based on its length
    result = max(final_list, key=len)
    print(result, len(result))

if __name__ == '__main__':
    array = [2, 6, 8, 3, 9, 1, 5, 6, 1, 3, 5, 7, 7, 1, 2, 3, 4, 5]
    longest_continuous_odd_subsequence(array)
