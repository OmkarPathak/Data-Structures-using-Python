# Author: OMKAR PATHAK

# Algorithm:
# 1) Create a set mstSet that keeps track of vertices already included in MST.
# 2) Assign a key value to all vertices in the input graph. Initialize all key values as INFINITE.
#    Assign key value as 0 for the first vertex so that it is picked first.
# 3) While mstSet doesn’t include all vertices
#    a) Pick a vertex u which is not there in mstSet and has minimum key value.
#    b) Include u to mstSet.
#    c) Update key value of all adjacent vertices of u. To update the key values, iterate through all adjacent
#      vertices. For every adjacent vertex v, if weight of edge u-v is less than the previous key value of v,
#      update the key value as weight of u-v

# Properties of Prim's Algorithm:
# 1) The edges in the subset of some minimum spanning tree always form a single tree.
# 2) It grows the tree until it spans all the vertices of the graph.
# 3) An edge is added to the tree, at every step, that crosses a cut if its weight is the minimum of any edge
#    crossing the cut, connecting it to a vertex of the graph.

import sys

class Graph(object):
    def __init__(self, vertices):
        self.vertices = vertices                        # Total number of Vertices in the graph
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]        # Initialize the adjacency matrix with zeros

    def getMinimumKey(self, weight, visited):
        # initialize the min by infinite number
        min = 9999

        for i in range(self.vertices):
            # Find the edge with minimum weight if it not visited
            if weight[i] < min and visited[i] == False:
                min = weight[i]
                minIndex = i

        # Return the index of the found edge with minimum weight
        return minIndex

    def primsAlgo(self):
        weight = [9999] * self.vertices     # This list will be used for storing the weights of all vertices
        MST = [None] * self.vertices        # This will contain our minimum spanning tree
        weight[0] = 0                       # Weight of the root node will be 0
        visited = [False] * self.vertices
        MST[0] = -1                         # Choosing first node as root vertex

        for _ in range(self.vertices):
            minIndex = self.getMinimumKey(weight, visited)
            # mark the index as visited
            visited[minIndex] = True

            for vertex in range(self.vertices):
                if self.graph[minIndex][vertex] > 0 and visited[vertex] == False and \
                weight[vertex] > self.graph[minIndex][vertex]:
                    weight[vertex] = self.graph[minIndex][vertex]
                    MST[vertex] = minIndex

        self.printMST(MST)

    def printMST(self, MST):
        print ("Edge \tWeight")
        for i in range(1, self.vertices):
            print (MST[i],"-",i,"\t",self.graph[i][ MST[i] ])

if __name__ == '__main__':
    g  = Graph(6)

    g.graph = [[0, 3, 2, 5, 7, 3],
               [3, 0, 4, 8, 6, 6],
               [2, 4, 0, 7, 1, 3],
               [5, 8, 7, 0, 2, 4],
               [7, 6, 1, 2, 0, 3],
               [3, 6, 3, 4, 3, 0]]

    g.primsAlgo()
