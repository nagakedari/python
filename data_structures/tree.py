class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
    def insert(self, node):
        if self.root:
            q = []
            q.append(self.root)
            while (len(q)>0):
                temp = q[0]
                q.pop(0)
                if temp.left == None:
                    temp.left = node
                    break
                else:
                    q.append(temp.left)
                if temp.right == None:
                    temp.right = node
                    break
                else:
                    q.append(temp.right)
        else:
            self.root = node
    
    def inorder_traversal(self, node):
        if node == None:
            return
        self.inorder_traversal(node.left)
        print(node.value, end=" ")
        self.inorder_traversal(node.right)

node = Node(1)
node1 = Node(2)
node2 = Node(3)
node3 = Node(4)
node4 = Node(5)
node5 = Node(6)
node6 = Node(7)
tree = Tree()
tree.insert(node)
tree.inorder_traversal(node)
print("\n")
tree.insert(node1)
tree.inorder_traversal(node)
print("\n")
tree.insert(node2)
tree.inorder_traversal(node)
print("\n")
tree.insert(node3)
tree.inorder_traversal(node)
print("\n")
tree.insert(node4)
tree.inorder_traversal(node)
print("\n")
tree.insert(node5)
tree.inorder_traversal(node)
print("\n")
tree.insert(node6)
tree.inorder_traversal(node)
print("\n")
