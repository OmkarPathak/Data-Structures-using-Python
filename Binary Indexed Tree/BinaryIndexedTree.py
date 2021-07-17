class BinaryIndexedTree:
    def __init__(self, arr):
        self.len = 1 + len(arr)
        self.tree = [0] * self.len # stores BIT
        self.orig = [0] * self.len # stores original array
        # build tree from values
        for i in range(len(arr)):
            self.update(i, arr[i])
    
    def update(self, i, diff):
        """
        Updates the value at index i by diff.
        """
        i += 1 # BIT is one-indexed
        self.orig[i] += diff # update original
        # update BIT
        while i < self.len:
            self.tree[i] += diff
            i += i & -i

    def query(self, i):
        """
        Returns the sum of arr[0..i], inclusive.
        """
        i += 1 # BIT is one-indexed
        ans = 0
        while i != 0:
            ans += self.tree[i]
            i -= i & -i
        return ans

    def get(self, i):
        """
        Get the element at position i
        """
        return self.orig[i + 1]

if __name__ == '__main__':
    bit = BinaryIndexedTree([4, 8, 4, 5, 6, 3, 2, 2, 8, 1])
    print('Sum of arr[0..4]:', bit.query(4))
    bit.update(2, -10) # decrease [2] by 10
    print('Sum of arr[0..4] after updating arr[2]:', bit.query(4))
    print('Value of arr[7]:', bit.get(7))
