def find_shortest_distance(graph, start_node):
    node_weight = {}
    infinity = 9999999
    for key in graph.keys():
        node_weight[key] = infinity
    node_weight[start_node] = 0
    unvisited = list(graph.keys())
    print(unvisited)
    shortest_distance = 0
    visited = set()
    while len(unvisited):
        node_with_min_distance = get_node_with_min_weight(node_weight, visited)
        print(node_with_min_distance)
        print(node_weight[node_with_min_distance])
        shortest_distance+= node_weight[node_with_min_distance]
        visited.add(node_with_min_distance)
        del unvisited[unvisited.index(node_with_min_distance)]
        adjucent_nodes = graph[node_with_min_distance]
        adjucent_node_with_min_distance = min(adjucent_nodes, key=adjucent_nodes.get)
        shortest_distance+=node_weight[adjucent_node_with_min_distance]
        node_weight[adjucent_node_with_min_distance]= shortest_distance
        node_with_min_distance = adjucent_node_with_min_distance  
    return shortest_distance

def get_node_with_min_weight(node_weight, visited):
    keys = list(node_weight.keys())
    i = 0
    min_weight = node_weight[keys[i]]
    min_weight_node = keys[i]
    if min_weight_node in visited:
        i+=1
        min_weight_node = keys[i]
    j= i+1
    while j < len(keys):
        if node_weight[keys[j]] < min_weight and node_weight[keys[j]]: 
            min_weight_node = keys[j]
        j+= 1
    return min_weight_node
graph = {
    'a': {'b':10, 'c':3},
    'b': {'c':1, 'd':2},
    'c': {'b':4, 'd':8, 'e':2},
    'd': {'e': 7},
    'e': {'d': 9}

}

find_shortest_distance(graph, 'a')