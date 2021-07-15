def find_shortest_distance(graph, start_node):
    node_weight = {}
    infinity = 9999999
    for key in graph.keys():
        node_weight[key] = infinity
    node_weight[start_node] = 0
    unvisited = list(graph.keys())
    print(unvisited)
    shortest_distance = 0
    q = []
    q.append(start_node)
    node_with_min_distance = min(node_weight, key=node_weight.get)
    shortest_distance+= node_weight[node_with_min_distance]
    while len(unvisited):
       
        print(node_with_min_distance)
        del unvisited[unvisited.index(node_with_min_distance)]
        adjucent_nodes = graph[node_with_min_distance]
        adjucent_node_with_min_distance = min(adjucent_nodes, key=adjucent_nodes.get)
        shortest_distance+=node_weight[adjucent_node_with_min_distance]
        node_weight[adjucent_node_with_min_distance]= shortest_distance
        node_with_min_distance = adjucent_node_with_min_distance
        # del node_weight[node_with_min_distance]
    return shortest_distance

graph = {
    'a': {'b':10, 'c':3},
    'b': {'c':1, 'd':2},
    'c': {'b':4, 'd':8, 'e':2},
    'd': {'e': 7},
    'e': {'d': 9}

}

find_shortest_distance(graph, 'a')