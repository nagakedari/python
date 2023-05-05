class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def height(root, h=0):
    if root:
        left_height = height(root.left, h)        
        right_height = height(root.right, h)
        h = 1 + max(left_height, right_height)
        return h
    else:
        return 0

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(height(root))
    root = TreeNode(1)
    root.right = TreeNode(2)
    print(height(root))