class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inverse_binary_tree(root):
    if root:
        root.left, root.right = root.right, root.left
        inverse_binary_tree(root.left)
        inverse_binary_tree(root.right)


def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val)
        inorder_traversal(root.right)



if __name__ == "__main__":
    root = Node(4)
    root.left = Node(2)
    root.right = Node(7)
    root.left.left = Node(1)
    root.left.right = Node(3)

    root.right.left = Node(6)
    root.right.right = Node(9)

    inorder_traversal(root)

    inverse_binary_tree(root)

    inorder_traversal(root)