class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root, traversed_list):
    if root:
        if root.left:
            traversed_list.append(root.left.val < root.val)
        inorder_traversal(root.left, traversed_list)
        if root.right:
            traversed_list.append(root.val < root.right.val)
        inorder_traversal(root.right, traversed_list)


def is_valid_bst(root):
    if root:
        traversed_list = []
        inorder_traversal(root, traversed_list)
        return all(traversed_list)
    return True


if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print(is_valid_bst(root))

    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)
    print(is_valid_bst(root))


