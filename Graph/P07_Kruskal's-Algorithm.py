# Author: OMKAR PATHAK

# A greedy algorithm example

# Algorithm:
# 1. T (the final spanning tree) is defined to be the empty set;
# 2. For each vertex v of G, make the empty set out of v;
# 3. Sort the edges of G in ascending (non-decreasing) order;
# 4. For each edge (u, v) from the sored list of step 3.
#       If u and v belong to different sets
#          Add (u,v) to T;
#          Get together u and v in one single set;
# 5. Return T

# from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    # function to add an edge to graph
    def addEdge(self, fromEdge, toEdge, weight):
        self.graph.append([fromEdge, toEdge, weight])

    # function to find the index of element i
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # function that finds the union of two sets first and second
    def union(self, parent, rank, first, second):
        root_x = self.find(parent, first)
        root_y = self.find(parent, second)

        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        # if ranks are same then increment its rank
        elif rank[root_x] == rank[root_y]:
            parent[root_y] = root_x
            rank[root_x] += 1

    def kruskals(self):
        result = []

        sortedIndex = 0
        resultIndex = 0

        # sort all the edges according to their weights inn ascending order
        self.graph =  sorted(self.graph,key=lambda item: item[2])

        parent = []
        rank = []

        for node in range(self.vertices):
            parent.append(node)
            rank.append(0)

        while resultIndex < self.vertices - 1:
            fromEdge, toEdge, weight = self.graph[sortedIndex]

            sortedIndex += 1
            root_x = self.find(parent, fromEdge)
            root_y = self.find(parent, toEdge)

            if root_x != root_y:
                resultIndex += 1
                result.append([fromEdge, toEdge, weight])
                self.union(parent, rank, root_x, root_y)

        # print the contents of result[] to display the built MST
        print ('Constructed Kruskal\'s Minimum Spanning Tree: ')
        for u,v,weight  in result:
            print('{} -> {} = {}'.format(u, v, weight))

if __name__ == '__main__':
    g = Graph(4)
    g.addEdge(0, 1, 10)
    g.addEdge(0, 2, 6)
    g.addEdge(0, 3, 5)
    g.addEdge(1, 3, 15)
    g.addEdge(2, 3, 4)

    g.kruskals()

    # OUTPUT:
    # Constructed Kruskal's Minimum Spanning Tree:
    # 2 -> 3 = 4
    # 0 -> 3 = 5
    # 0 -> 1 = 10
