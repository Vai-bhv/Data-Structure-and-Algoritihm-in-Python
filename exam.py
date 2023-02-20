class Graph:
 
    # init function to declare class variables
    def __init__(self, V):
        self.V = V
        self.joint = [[] for i in range(V)]
 
    def DFSUtil(self, hold, v, visit):
 
        # Mark the current vertex as visit
        visit[v] = True
 
        # Store the vertex to list
        hold.append(v)
 
        # Repeat for all vertices adjacent
        # to this vertex v
        for i in self.joint[v]:
            if visit[i] == False:
 
                # Update the list
                hold = self.DFSUtil(hold, i, visit)
        return hold
 
    # method to add an undirected edge
    def addEdge(self, v, w):
        self.joint[v].append(w)
        self.joint[w].append(v)
 
    # Method to retrieve connected components
    # in an undirected graph
    def con_comp(self):
        visit = []
        connected_components = []
        for i in range(self.V):
            visit.append(False)
        for v in range(self.V):
            if visit[v] == False:
                hold = []
                connected_components.append(self.DFSUtil(hold, v, visit))
        return connected_components
 
 

g = Graph(11)
g.addEdge(1, 2)
g.addEdge(5, 9)
g.addEdge(4, 6)
g.addEdge(1, 8)
g.addEdge(8, 2)
g.addEdge(7, 6)
g.addEdge(2, 10)
connected_components = g.con_comp()
print(connected_components)



# n = int(input())
# m = int(input())
# g = Graph(n+1)


# connected_components = g.con_comp()
# print(connected_components)