import Heap

def findKthLargestElement(nums:list,k:int):
    '''
    The problem here is to find the Kth Largest Element from the array.
    to solve this we could've used sort and given the answer but it would've cost us O(N*logN) where N is the number of elements in the array

    to even optimize that solution we can use heaps.
    the idea here is:
    1. create a min-heap with adding all the values as negative to it
    2. deleting till second last step
    3. returning the element at the last step as the answer

    T - O(N +K*log(N)) where K is the position of Kth largest element and N is the number of elements in the array

    '''
    h=Heap.BinaryHeap()
    [h.insert(-num) for num in nums]
    [h.delete() for _ in range(k-1)]

    return -h.delete()


if __name__ == '__main__':
    
    nums=[2,3,5,6,4]
    k=2
    kthLargestElement = findKthLargestElement(nums,k)

    print("the Kth("+str(k)+") largest element is",kthLargestElement)