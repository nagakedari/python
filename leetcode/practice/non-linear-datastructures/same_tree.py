class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_same_tree(root1, root2):
    if not root1 and not root2:
        return True
    elif not root1 or not root2:
        return False
    elif root1.val != root2.val:
        return False
    is_left_same = is_same_tree(root1.left, root2.left)
    is_right_same = is_same_tree(root1.right, root2.right)
    return is_left_same and is_right_same


if __name__ == "__main__":
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)

    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)

    print(is_same_tree(root1, root2))

    root1 = TreeNode(1)
    root1.left = TreeNode(2)

    root2 = TreeNode(1)
    root2.right = TreeNode(2)

    print(is_same_tree(root1, root2))