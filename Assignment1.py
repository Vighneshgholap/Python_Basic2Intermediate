############################################################################################
# ASSIGNMENT 1: UNINFORMED SEARCH PROBLEM
# Vighnesh Gholap, USF: 1/24/2023
############################################################################################
graph = {
    '2':{'13':3, '8':16},
    '13':{'2':5, '1':12, '5':4},
    '1':{'8':20},
    '3':{'1':10},
    '5':{'3':6, '8':5},
    '8':{'13':13}
}
# Variables needed
vertex = {}                     # stores all the vertices
edge = {}                       # stores the final path
unseen_vertex = graph           # to work on graph elements without changing graph
inf = 99999                     # a big number to show infinity when there is no edges
track = []                      # track the path/ subject to change and update

# user input
start = input("Start vertex: ")
goal = input("Destination vertex: ")

def search():
    # Actual process to check the shortest path:
    while unseen_vertex:
        # during the new search, we dont know what the edge weight is so,
        next_vertex = None          # This will be our first Vertex distance
        
        # One search for the shortest path
        for curr_vertex in unseen_vertex:
            # for the very First search:
            if next_vertex is None:
                next_vertex = curr_vertex

            # Else if its not the first search ie. its not the src vertex
            # if A -> B is 3 (curr_vertex) and A-> C is 4 (min dist) : now min dist is 3
            elif vertex[curr_vertex] < vertex[next_vertex]:
                next_vertex = curr_vertex
        # dic will have the leements of the path: '2','13','5','8'        
        dic = graph[next_vertex].items()

        for child_node, weight in dic:
            # if we find another optimal option, we will replace our list
            if weight + vertex[next_vertex] < vertex[child_node]:
                vertex[child_node] = weight + vertex[next_vertex]
                edge[child_node] = next_vertex
        
        unseen_vertex.pop(next_vertex)
def printFunc():
    if vertex[goal] != inf:
        print()
        print("Shortest distance is: " + str(vertex[goal]))
        print()
        print("Optimal track is: ")
    for i in range(len(track)):
        try:
            print("Vertex " + (track[i]) + " to vertex " + (track[i+1]))
        except IndexError:
            break
    print()

def dijkstra(graph,start,goal):
    

    # first we assign the source to 0 and rest unseen vertices to infinity
    for curr_vertex in unseen_vertex:
        vertex[curr_vertex] = inf
    vertex[start] = 0

    search()    # Call our search function

    # the last vertex should be our goal vertex
    present = goal
    while present != start:
        try:
            track.insert(0, present)
            present = edge[present]
        except KeyError:
            print("track is not reachable")
            break
    
    track.insert(0,start)

    printFunc() # call our print function
        
dijkstra(graph, start, goal)
