#  A program to check whether the string contains equal & same no of characters
import collections


def check_strings(word1, word2):
    word1 = list(word1)
    word2 = list(word2)
    dict1 = {}
    dict2 = {}
    flag = True
    for i in word1:
        if i in dict1:
            dict1[i] = dict1[i] + 1
            continue
        else:
            dict1[i] = 1
    for i in word2:
        if i in dict2:
            dict2[i] = dict2[i] + 1
            continue
        else:
            dict2[i] = 1
    if len(dict1) == len(dict2):
        for k, v in dict1.items():
            if k in dict2:
                if dict2[k] == v:
                    continue
                else:
                    flag = False
                    break
            else:
                flag = False
                break
    if flag:
        print("Same")
    else:
        print("Not Same")


def main():
    word1 = input("Enter first string : ")
    word2 = input("Enter second string : ")
    check_strings(word1, word2)
    word = "madam"


main()
