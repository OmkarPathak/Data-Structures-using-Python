# A python program to calculate the frequency of each character in the string
def count_frquency(word):
    val=dict()
    word=list(word)
    for i in word:
        if i in val:
            val[i]=val[i]+1
            continue
        else:
            val[i]=1
    print(word)
    return val


def main():
    word=input("Enter a string whose frequency you want to calculate ")
    print(word)
    print("Frequency of respective characters in {0} is {1}".format(word,count_frquency(word)))

main()

