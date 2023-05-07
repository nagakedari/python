class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lca(root, p, q):
    if root:
        # if p == root.val or q == root.val:
        #     return root.val
        # elif p < root.val and q > root.val:
        #     return root.val
        # elif p < root.val and q < root.val:
        #     return lca(root.left, p, q)
        # else:
        #     return lca(root.right, p, q)
        if p < root.val and q < root.val:
            return lca(root.left, p, q)
        elif p > root.val and q > root.val:
            return lca(root.right, p, q)
        else:
            return root.val

if __name__ == "__main__":
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)

    print(lca(root, 2, 8))
    print(lca(root, 2, 4))

    root = TreeNode(2)
    root.left = TreeNode(1)
    print(lca(root, 2, 1))

