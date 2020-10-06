'''
This creates a BALANCED BST from an unsorted array.

Tree() is a class create instance of a root node. (This is already implemented in other files in the repo)
'''

def toBst(arr):
    arr.sort()
    def toBalanced(arr):
        if(not arr):
            return None

        mid=len(arr)//2
        root=Tree(arr[mid])
        root.left=toBalanced(arr[0:mid])
        root.right=toBalanced(arr[mid+1:])

        return root
    return toBalanced(arr) 
