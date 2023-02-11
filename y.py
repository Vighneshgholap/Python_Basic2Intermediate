graph = {
    '2':{'13':3, '8':16},
    '13':{'2':5, '1':12, '5':4},
    '1':{'8':20},
    '3':{'1':10},
    '5':{'3':6, '8':5},
    '8':{'13':13}
}
start = input("Start vertex: ")
goal = input("Destination vertex: ")

def dijkstra(graph,start,goal):
    vertex = {}                 # stores all the vertices
    edge = {}
    unseen_vertex = graph       # to work on graph elements without changing graph
    inf = 99999                 # a big number to show infinity whien there is no edges
    track = []                  # track the path/ subject to change and update

    # first we assign the source to 0 and rest unseen vertices to infinity
    vertex[start] = 0
    for curr_vertex in unseen_vertex:
        vertex[curr_vertex] = inf
    
    # Actual process to check the shortest path:
    while unseen_vertex:
        # during the new search, we dont know what the edge weight is so,
        next_vertex = None      # This will be our first Vertex distance

        # One search for the shortest path
        for curr_vertex in unseen_vertex:
            # for the very First search:
            if next_vertex is None:
                next_vertex = curr_vertex
            # Else if its not the first search ie. its not the src vertex
            # if A -> B is 3 (curr_vertex) and A-> C is 4 (min dist) : now min dist is 3
            elif vertex[curr_vertex] < vertex[next_vertex]:
                next_vertex = curr_vertex
        dic = graph[next_vertex].items()
        for child_vertex, weight in dic:
            if weight + vertex[next_vertex] < vertex[child_vertex]:
                vertex[child_vertex] = vertex[next_vertex] + weight
                edge[child_vertex] = next_vertex
        unseen_vertex.pop(next_vertex)
    
    present = goal
    while present != start:
        try:
            track.insert(0,present)
            present = edge[present]
        except KeyError:
            print("Error")
            break
    
    track.insert(0,start)

    if vertex[goal] != inf:
        print("Shortest distance is: " + str(vertex[goal]))
        print("Optimal track is: ")
    for i in range(len(track)):
        try:
            print("Vertex " + (track[i]) + " to vertex " + (track[i+1]))
        except IndexError:
            break

dijkstra(graph, start, goal)
