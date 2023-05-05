import collections

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sub_tree_of_a_tree(root1, root2):
    q = collections.deque()
    q.append(root1)

    while q:
        node = q.popleft()
        print(node.val)
        print(root2.val)
        if node.val == root2.val:
            break
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)


    def are_trees_identical(root1, root2):
        if root1 is None and root2 is None:
            return True
        elif root1 is None or root2 is None:
            return False
        elif root1.val != root2.val:
            return False
        return are_trees_identical(root1.left, root2.left) and are_trees_identical(root1.right, root2.right)
    print(node.val)
    return are_trees_identical(node, root2)

if __name__ == "__main__":
    root1 = TreeNode(3)
    root1.left = TreeNode(4)
    root1.right = TreeNode(5)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(2)

    root2 = TreeNode(4)
    root1.left = TreeNode(1)
    root1.right = TreeNode(2)

    print(sub_tree_of_a_tree(root1, root2))

    root1 = TreeNode(3)
    root1.left = TreeNode(4)
    root1.right = TreeNode(5)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(2)
    root1.left.right.left = TreeNode(0)

    root2 = TreeNode(4)
    root1.left = TreeNode(1)
    root1.right = TreeNode(2)

    print(sub_tree_of_a_tree(root1, root2))

