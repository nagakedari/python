import collections


class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node):
    old_to_new = {}

    # def dfs(node):
    #     if node in old_to_new:
    #         return old_to_new[node]
    #     copy = Node(node.val)
    #     old_to_new[node] = copy
    #     for nei in node.neighbors:
    #         copy.neighbors.append(dfs(nei))
    #     return copy
    # return dfs(node) if node else None

    def bfs(node):
        q = collections.deque()
        q.append(node)

        while q:
            n = q.popleft()
            copy = Node(n.val)
            for nei in node.neighbors:
                if nei not in old_to_new:
                    old_to_new[nei] = Node(nei.val)
                    q.append(nei)

                copy.neighbors.append(old_to_new[nei])
    return bfs(node) if node else None