# Max heap implementation

# runs in linear time
def heapify(A):
    '''Turns a list `A` into a max-ordered binary heap.'''
    n = len(A) - 1
    # start at last parent and go left one node at a time
    for node in range(n/2, -1, -1):
        __shiftdown(A, node)
    return

# runs in log(n) time
def push_heap(A, val):
    '''Pushes a value onto the heap `A` while keeping the heap property
    intact.  The heap size increases by 1.'''
    A.append(val)
    __shiftup(A, len(A) - 1)   # furthest left node
    return

# runs in log(n) time
def pop_heap(A):
    '''Returns the max value from the heap `A` while keeping the heap
    property intact.  The heap size decreases by 1.'''
    n = len(A) - 1
    __swap(A, 0, n)
    max = A.pop(n)
    __shiftdown(A, 0)
    return max

# runs in log(n) time
def replace_key(A, node, newval):
    '''Replace the key at node `node` in the max-heap `A` by `newval`.
    The heap size does not change.'''
    curval  = A[node]
    A[node] = newval
    # increase key
    if newval > curval:
        __shiftup(A, node)
    # decrease key
    elif newval < curval:
        __shiftdown(A, node)
    return

def __swap(A, i, j):
    # the pythonic swap
    A[i], A[j] = A[j], A[i]
    return

# runs in log(n) time
def __shiftdown(A, node):
    '''Traverse down a binary tree `A` starting at node `node` and
    turn it into a max-heap'''
    child = 2*node + 1
    # base case, stop recursing when we hit the end of the heap
    if child > len(A) - 1:
        return
    # check that second child exists; if so find max
    if (child + 1 <= len(A) - 1) and (A[child+1] > A[child]):
        child += 1
    # preserves heap structure
    if A[node] < A[child]:
        __swap(A, node, child)
        __shiftdown(A, child)
    else:
        return

# runs in log(n) time
def __shiftup(A, node):
    '''Traverse up an otherwise max-heap `A` starting at node `node`
    (which is the only node that breaks the heap property) and restore
    the heap structure.'''
    parent = (node - 1)/2
    if A[parent] < A[node]:
        __swap(A, node, parent)
    # base case; we've reached the top of the heap
    if parent <= 0:
        return
    else:
        __shiftup(A, parent)
