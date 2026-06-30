class Graph:
    def __init__(self, nv):
        self._nv=nv
        self.adj_list=[]
        for i in range(nv):
            self.adj_list.append([])
    
    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def print_graph(self):
        for i in range(self._nv):
            print(i, end=": ")
            for j in range(len(self.adj_list[i])):
                print(self.adj_list[i][j],end=" ")
            print("\n")
'''def DFS(g, u, discovered):
    for e in g.incident_edges(u):
        v=e.opposite(u)
        if v not in discovered:
            discovered[v]=e
            DFS(g, v, discovered)'''

g=Graph(5)
g.add_edge(0,1)
g.add_edge(0,3)
g.add_edge(1,2)
g.add_edge(1,4)
g.print_graph()