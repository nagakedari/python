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
    
    def pre_traversal(self, node):
        if node:
            print(node.value, end=" ")
            self.pre_traversal(node.left)
            self.pre_traversal(node.right)
        return
    def post_traversal(self, node):
        if node:
            self.post_traversal(node.left)
            self.post_traversal(node.right)
            print(node.value, end=" ")
        return
        
    def inorder_print(self, node, traversal):
        if node:
            traversal = self.inorder_print(node.left, traversal)
            traversal+= (str(node.value)+'-')
            traversal = self.inorder_print(node.right,traversal)
        return traversal
    def height(self, root):
        if root:
            return 1+ max(self.height(root.left), self.height(root.right))
        else: 
            return 0
    def vertical_traversal(self):
        traversal = {}
        if self.root:
            self.get_nodes_for_each_depth(self.root, 0, traversal)    
        for index, values in enumerate(sorted(traversal)):
            for i in traversal[values]:
                print(i)
        return 
    def get_nodes_for_each_depth(self, node, depth, traversal):
        if node:
            if depth in traversal.keys():
                traversal[depth].append(node.value)
            else:
                traversal[depth] = [node.value]
            self.get_nodes_for_each_depth(node.left, depth-1, traversal)
            self.get_nodes_for_each_depth(node.right, depth+1, traversal )
        return
    def my_level_order_traversal(self, node):
        if node:
            if node.value == self.root.value:
                print(node.value)
            if node.left:
                print(node.left.value)
            if node.right:
                print(node.right.value)
            self.my_level_order_traversal(node.left)
            self.my_level_order_traversal(node.right)
        return
    def level_order_traversal(self):
        for l in range(1, self.height(self.root)+1):
            self.printCurrentLevelNodes(self.root, l)

    def printCurrentLevelNodes(self, node, l):
        if node == None:
            return
        if l==1:
            print(node.value)
        elif l > 1:
            self.printCurrentLevelNodes(node.left, l-1)
            self.printCurrentLevelNodes(node.right, l-1)

node = Node(1)
node1 = Node(2)
node2 = Node(3)
node3 = Node(4)
node4 = Node(5)
node5 = Node(6)
node6 = Node(7)
tree = Tree()
tree.insert(node)
# tree.inorder_traversal(node)
# print("\n")
tree.insert(node1)
# tree.inorder_traversal(node)
# print("\n")
tree.insert(node2)
# tree.inorder_traversal(node)
# print("\n")
tree.insert(node3)
# tree.inorder_traversal(node)
# print("\n")
tree.insert(node4)
# tree.inorder_traversal(node)
# print("\n")
tree.insert(node5)
# tree.inorder_traversal(node)
# print("\n")
tree.insert(node6)
# tree.inorder_traversal(node)
# print("\n")

# print(tree.inorder_print(node, ''))

# print(tree.height(node))
# print("\n")
# tree.pre_traversal(node)
# print("\n")
# tree.post_traversal(node)

# tree.level_order_traversal()

tree1 = Tree()

tree1.root=node
node.left = node1
node.right = node2
node.left.left = node3
node.left.right = node4
node.right.left = node5
node.right.right = node6
node.right.left.right = Node(8)
node.right.right.right = Node(9)

tree1.vertical_traversal()
# tree1.my_level_order_traversal(node)

