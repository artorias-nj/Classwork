from collections import defaultdict
 
# Build the Graph
def build_graph():
    edges = [
        ["A", "B"], ["A", "C"],
        ["B", "D"], ["B", "E"],
        ["C", "D"], ["D", "E"]
        
    ]
    graph = defaultdict(list)
     

    for edge in edges:
        a, b = edge[0], edge[1]
         

        graph[a].append(b)
        graph[b].append(a)
    return graph
 
     
#find the shortest path
def findpath(graph, start, end):
    explored = []
     

    queue = [[start]]
     

    if start == end:
        print("Same Node")
        return
     

    while queue:
        path = queue.pop(0)
        node = path[-1]
         

        if node not in explored:
            neighbours = graph[node]
             

            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                 

                if neighbour == end:
                    print("Shortest path = ", *new_path)
                    return
            explored.append(node)
 

    print("There is no path")
    return

#create graph    
g = build_graph()

#print graph  
print(g)

#test graph
findpath(g, "A", "E")
findpath(g, "D", "A")
findpath(g, "E", "C")
findpath(g, "B", "C")