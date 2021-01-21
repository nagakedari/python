class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        self.height = 1
class AvlTree:
    def __init__(self):
        self.root = None
    def insert(self, root, value):
        if root is None:
            return Node(value)
        elif value < root.val:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)
        
        root.height = self.height(root)
        balance_factor = self.height(root.left) - self.height(root.right)

        if balance_factor > 1 and value < root.left.val:
            #left-left
            return self.rotate_right(root)
        elif balance_factor > 1 and value > root.left.val:
            #left-right
            root.left= self.rotate_left(root.left)
            return self.rotate_right(root)
        elif balance_factor < -1 and value < root.right.val:
            #right-left
            root.right= self.rotate_right(root.right)
            return self.rotate_left(root)
        elif balance_factor < -1 and value > root.right.val:
            #right-right
            return self.rotate_left(root)

        return root

    def height(self, root):
        if root:
            return 1 + max(self.height(root.left), self.height(root.right))
        else:
            return 0
    def rotate_right(self, root):
        z = root
        y = root.left
        z.left = y.right
        y.right = z
        z.height = self.height(z)
        y.height = self.height(y)
        return y
        
    def rotate_left(self, root):
        z = root
        y = root.right
        z.right = y.left
        y.left = z
        z.height = self.height(z)
        y.height = self.height(y)
        return y

    def preorder_traversal(self, root):
        if root is None:
            return
        print(root.val, end=" ")
        self.preorder_traversal(root.left)
        self.preorder_traversal(root.right)


myTree = AvlTree() 
root = None
root = myTree.insert(root, 10) 
root = myTree.insert(root, 20) 
root = myTree.insert(root, 30) 
root = myTree.insert(root, 40) 
root = myTree.insert(root, 50) 
root = myTree.insert(root, 25)

myTree.preorder_traversal(root)