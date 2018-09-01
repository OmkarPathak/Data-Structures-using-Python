# Author: OMKAR PATHAK
# Edited and corrected by: Rahul Jain(rahuldkjain)
class Graph():
    def __init__(self):
        self.vertex = {}
        self.noOfNodes = 0

    # for printing the Graph vertexes
    def printGraph(self):
        print(self.vertex)
        for i in self.vertex.keys():
            print(i,' -> ', ' -> '.join([str(j) for j in self.vertex[i]]))

    # for adding the edge beween two vertexes
    def addEdge(self, fromVertex, toVertex):
        # check if vertex is already present,
        if fromVertex in self.vertex.keys():
            self.vertex[fromVertex].append(toVertex)
        else:
            # else make a new vertex
            self.vertex[fromVertex] = [toVertex]

    def DFS(self):
        # visited array for storing already visited nodes
        visited = [False] * self.noOfNodes

        # call the recursive helper function
        for i in range(len(self.vertex)):
            if visited[i] == False:
                self.DFSRec(i, visited)

    def DFSRec(self, startVertex, visited):
        # mark start vertex as visited
        visited[startVertex] = True

        print(startVertex, end = ' ')

        # Recur for all the vertexes that are adjacent to this node
        if startVertex in self.vertex.keys():
          adjacentNodes = self.vertex[startVertex]
          for i in adjacentNodes:
            if visited[i] == False:
                self.DFSRec(i, visited)

if __name__ == '__main__':
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    g.noOfNodes = 4
    g.printGraph()
    print('DFS:')
    g.DFS()
