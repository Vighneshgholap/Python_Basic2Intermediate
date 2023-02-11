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
    vertex = {} # a list that has the cost to reach to specific node
    track_predecessor = {} # a list  that record of the path
    unseenNodes = graph
    inf = 10000 # lasrge number for the self vertex
    #path = [] # our final anser
    track_path = []
    # assign the start vertex distance to 0
    
    # assign the rest vertex to infinity 
    for node in unseenNodes:
        vertex[node] = inf
    vertex[start] = 0
    # go through all the vertex and track_predecessor
    while unseenNodes:
        min_dis = None
        
        for node in unseenNodes:
            if min_dis is None:
                min_dis = node
            elif vertex[node] < vertex[min_dis]:
                min_dis = node
        path_options = graph[min_dis].items()
        for chile_node, weight in path_options:
            if weight + vertex[min_dis] < vertex[chile_node]:
                vertex[chile_node] = weight + vertex[min_dis]
                track_predecessor[chile_node] = min_dis
        
        unseenNodes.pop(min_dis)

    currentNode = goal

    while currentNode != start:
        try:
            track_path.insert(0, currentNode)
            currentNode = track_predecessor[currentNode]
        except KeyError:
            print("Path is not reachable")
            break
    
    track_path.insert(0,start)

    if vertex[goal] != inf:
        print("Shortest distance is: " + str(vertex[goal]))
        print("Optimal path is: " + str(track_path))

dijkstra(graph, start, goal)
