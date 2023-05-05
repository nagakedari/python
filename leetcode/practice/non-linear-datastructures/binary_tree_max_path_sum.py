class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_path_sum(root):
    res = [root.val]

    def dfs(root):
        if not root: return 0
        left_max = dfs(root.left)
        right_max = dfs(root.right)

        left_max = max(left_max, 0)
        right_max = max(right_max, 0)

        res[0] = max(res[0], root.val + left_max + right_max)

        return root.val + max(left_max, right_max)

    dfs(root)

    return res[0]

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    print(max_path_sum(root))

    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(max_path_sum(root))

    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.left.left = TreeNode(40)
    root.left.right = TreeNode(10)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(max_path_sum(root))
