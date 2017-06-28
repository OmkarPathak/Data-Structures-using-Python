# Author: OMKAR PATHAK

# Time Complexity: O(|V| + |E|)

class Graph():
    def __init__(self):
        self.vertex = {}

    # for printing the Graph vertexes
    def printGraph(self):
        for i in self.vertex.keys():
            print(i,' -> ', ' -> '.join([str(j) for j in self.vertex[i]]))

    # for adding the edge beween two vertexes
    def addEdge(self, fromVertex, toVertex):
        # check if vertex is already present,
        if fromVertex in self.vertex.keys() and toVertex in self.vertex.keys():
            self.vertex[fromVertex].append(toVertex)
            self.vertex[toVertex].append(fromVertex)
        else:
            # else make a new vertex
            self.vertex[fromVertex] = [toVertex]
            self.vertex[toVertex] = [fromVertex]

    # This function will return True if graph is cyclic else return False
    def checkCyclic(self):
        visited = [False] * len(self.vertex)            # Marking all vertices as not visited
        for vertex in range(len(self.vertex)):
            # Call the recursive function only if not visited
            if visited[vertex] == False:
                if self.checkCyclicRec(visited, -1, vertex) == True:
                    return True
        return False

    # Recursive function for finding the cycle
    def checkCyclicRec(self, visited, parent, vertex):
        # Mark the current node in visited
        visited[vertex] = True

        # mark all adjacent nodes of the current node
        for adjacentNode in self.vertex[vertex]:
            if visited[adjacentNode] == False:
                if self.checkCyclicRec(visited, vertex, adjacentNode) == True:
                    return True
            elif parent != adjacentNode:
                return True

        return False

if __name__ == '__main__':
    graph = Graph()
    graph.addEdge(0, 1)
    graph.addEdge(0, 2)
    graph.addEdge(1, 2)
    graph.addEdge(2, 0)
    graph.addEdge(2, 3)
    graph.addEdge(3, 3)

    graph.printGraph()

    if graph.checkCyclic() == 1:
        print ("Graph has a cycle")
    else:
        print ("Graph has no cycle")

    g1 = Graph()
    g1.addEdge(0,1)
    g1.addEdge(1,2)

    g1.printGraph()

    if g1.checkCyclic() == 1:
        print ("Graph has a cycle")
    else:
        print ("Graph has no cycle")

    # OUTPUT:
    # 0  ->  2 -> 2
    # 1  ->  0 -> 2
    # 2  ->  3
    # 3  ->  2 -> 3 -> 3
    # Graph has a cycle
    # 0  ->  1
    # 1  ->  2
    # 2  ->  1
    # Graph has no cycle
