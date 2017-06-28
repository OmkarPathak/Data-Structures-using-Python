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
        if fromVertex in self.vertex.keys():
            self.vertex[fromVertex].append(toVertex)
        else:
            # else make a new vertex
            self.vertex[fromVertex] = [toVertex]

    # This function will return True if graph is cyclic else return False
    def checkCyclic(self):
        visited = [False] * len(self.vertex)
        stack = [False] * len(self.vertex)
        for vertex in range(len(self.vertex)):
            if visited[vertex] == False:
                if self.checkCyclicRec(visited, stack, vertex) == True:
                    return True
        return False

    # Recursive function for finding the cycle
    def checkCyclicRec(self, visited, stack, vertex):
        # Mark the current node in visited and also add it to the stack
        visited[vertex] = True
        stack[vertex] = True

        # mark all adjacent nodes of the current node
        for adjacentNode in self.vertex[vertex]:
            if visited[adjacentNode] == False:
                if self.checkCyclicRec(visited, stack, adjacentNode) == True:
                    return True
            elif stack[adjacentNode] == True:
                return True

        # The node needs to be poped from
        # recursion stack before function ends
        stack[vertex] = False
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
