# Author: OMKAR PATHAK

class Array(object):
    ''' size_of_array: denotes the total size of the array to be initialized
       array_type: denotes the data type of the array(as all the elements of the array have same data type)
       array_items: values at each position of array
    '''
    def __init__(self, size_of_array, array_type = int):
        self.size_of_array = len(list(map(array_type, range(size_of_array))))
        self.array_items =[array_type(0)] * size_of_array    # initialize array with zeroes
        self.array_type = array_type

    def __str__(self):
        return ' '.join([str(i) for i in self.array_items])

    def __len__(self):
        return len(self.array_items)

    # magic methods to enable indexing
    def __setitem__(self, index, data):
        self.array_items[index] = data

    def __getitem__(self, index):
        return self.array_items[index]

    # function for search
    def search(self, key_to_search):
        for i in range(self.size_of_array):
            if (self.array_items[i] == key_to_search):      # brute-forcing
                return i                                 # index at which element/ key was found

        return -1                                        # if key not found, return -1

    # function for inserting an element
    def insert(self, key_to_insert, position):
        if(self.size_of_array > position):
            for i in range(self.size_of_array - 2, position - 1, -1):
                self.array_items[i + 1] = self.array_items[i]
            self.array_items[position] = key_to_insert
        else:
            print('Array size is:', self.size_of_array)

    # function to delete an element
    def delete(self, keyToDelete, position):
        if(self.size_of_array > position):
            for i in range(position, self.size_of_array - 1):
                self.array_items[i] = self.array_items[i + 1]
            self.array_items[i + 1] = self.array_type(0)
        else:
            print('Array size is:', self.size_of_array)

if __name__ == '__main__':
    a = Array(10, int)
    a.insert(2, 2)
    a.insert(3, 1)
    a.insert(4,7)
    print(len(a))
