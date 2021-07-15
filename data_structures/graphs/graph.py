class Node:
    def __init__(self, value):
        self.value = value
        self.edges = []
class Edge:
    def __init__(self, value,fromNode, toNode):
        self.value = value
        self.fromNode = fromNode
        self.toNode = toNode

class Graph:

    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges
    
    def insert_node(self, new_node_val):
        new_node = Node(new_node_val)
        self.nodes.append(new_node)
    
    def insert_edge(self, value, fromNodeVal, toNodeVal):
        from_node_found = None
        to_node_found = None
        
        for node in self.nodes:
            if node.value == fromNodeVal:
                from_node_found = node
            if node.value == toNodeVal:
                to_node_found = node
        if from_node_found == None:
            from_node_found = Node(fromNodeVal)
            self.nodes.append(from_node_found)
        if to_node_found == None:
            to_node_found = Node(toNodeVal)
            self.nodes.append(to_node_found)

        new_edge = Edge(value, from_node_found, to_node_found)
        self.edges.append(new_edge)
        from_node_found.edges.append(new_edge)
        to_node_found.edges.append(new_edge)
    
    def get_edge_list(self):
        edge_list = []
        for edge in self.edges:
            edge_list.append((edge.value, edge.fromNode.value, edge.toNode.value))
        return edge_list

    def get_adjacency_list(self):
        adjacency_list = []
        dictionary = {}
        for edge in self.edges:
            if edge.fromNode.value in dictionary:
                if edge.toNode:
                    dictionary[edge.fromNode.value].append((edge.toNode.value, edge.value))
            else:
                if edge.toNode:
                    dictionary[edge.fromNode.value] = [(edge.toNode.value, edge.value)]
        for i in range(0, len(self.edges)+1):
            if i in dictionary.keys():
                adjacency_list.append(dictionary[i])
            else:
                adjacency_list.append(None)
        return adjacency_list

    def get_adjacency_matrix(self):
        adjucency_list = self.get_adjacency_list()
        adjucency_matrix = []
        for adjucency in adjucency_list:
            sub_list=[]
            if adjucency:
                dictionary = {}
                for i, edge in enumerate(adjucency):
                    if edge[0] not in dictionary.keys():
                        dictionary[edge[0]] = edge[1]
                for i in range(0, len(adjucency_list)):
                    if i in dictionary.keys():
                        sub_list.append(dictionary[i])
                    else:
                         sub_list.append(0)
            else:
                for i in range(0, len(adjucency_list)):
                    sub_list.append(0)
            adjucency_matrix.append(sub_list)
        return adjucency_matrix

    def get_adjacency_matrix_better(self):
        # max_index = self.find_max_index()
        adjacency_matrix = [[0 for i in range(len(self.nodes) + 1)] for j in range(len(self.nodes) + 1)]
        for edge_object in self.edges:
            adjacency_matrix[edge_object.fromNode.value][edge_object.toNode.value] = edge_object.value
        return adjacency_matrix
    
    def find_shortest_path(self, start, end):
        q = []
        node = self.get_node_by_value(start)
        q.append(node)
        visited = []
        intermidiate_path = [start]
        while (len(q)):
            node = q.pop(0)
            path = intermidiate_path.pop(0)
            if node:
                if node not in visited:
                    neighbors = node.edges
                    for neighbor in neighbors:
                        new_path = list(path)
                        new_path.append(neighbor.toNode.value)
                        q.append(neighbor.toNode)
                        intermidiate_path.append(new_path)
                        if neighbor.toNode.value == end:
                            print('Shortest path: {}'.format(new_path))
                            return
                    visited.append(node)

    def get_node_by_value(self, value):
        for node in self.nodes:
            # print(value)
            print(node.value)
            if node.value == value:
                return node
        return None

    # def find_max_index(self):
    #     max_index = -1
    #     if len(self.nodes):
    #         for node in self.nodes:
    #             if node.value > max_index:
    #                 max_index = node.value
    #     return max_index

# graph = Graph()
# graph.insert_edge(100, 1, 2)
# graph.insert_edge(101, 1, 3)
# graph.insert_edge(102, 1, 4)
# graph.insert_edge(103, 3, 4)
# # Should be [(100, 1, 2), (101, 1, 3), (102, 1, 4), (103, 3, 4)]
# print(graph.get_edge_list())
# # Should be [None, [(2, 100), (3, 101), (4, 102)], None, [(4, 103)], None]
# print(graph.get_adjacency_list())
# # Should be [[0, 0, 0, 0, 0], [0, 0, 100, 101, 102], [0, 0, 0, 0, 0], [0, 0, 0, 0, 103], [0, 0, 0, 0, 0]]
# print(graph.get_adjacency_matrix())
# print(graph.get_adjacency_matrix_better())


graph1 = Graph()

graph1.insert_edge(1, 'A', 'B')
graph1.insert_edge(2, 'A', 'E')
graph1.insert_edge(4, 'A', 'C')
graph1.insert_edge(2, 'B', 'D')
graph1.insert_edge(3, 'B', 'E')
graph1.insert_edge(1, 'B', 'A')
graph1.insert_edge(2, 'D', 'B')
graph1.insert_edge(5, 'D', 'E')
graph1.insert_edge(2, 'E', 'A')
graph1.insert_edge(3, 'E', 'B')
graph1.insert_edge(4, 'C', 'A')
graph1.insert_edge(6, 'C', 'F')
graph1.insert_edge(7, 'C', 'G')
graph1.insert_edge(6, 'F', 'C')
graph1.insert_edge(7, 'G', 'C')

print(len(graph1.nodes))

graph1.find_shortest_path('F', 'G')

