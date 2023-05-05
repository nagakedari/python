class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class SdBinaryTree:
    def serialize(self, root):
        serialized_string = []
        def preorder(root, serialized_string):
            if root:
                serialized_string.append(str(root.val))
                preorder(root.left, serialized_string)
                preorder(root.right, serialized_string)
            else:
                serialized_string.append('N')

        preorder(root, serialized_string)
        return ','.join(serialized_string)


    def deserialize(self, serialized_string):
        nodes = serialized_string.split(',')
        print(nodes)
        self.index = 0
        def dfs():
            if nodes[self.index] == "N":
                self.index += 1
                return None
            node = TreeNode(int(nodes[self.index]))
            self.index += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    ser = SdBinaryTree()
    serialized_string = ser.serialize(root)

    print(serialized_string)

    deserialized_tree = []

    def preorder(root, deserialized_tree):
        if root:
            deserialized_tree.append(root.val)
            preorder(root.left, deserialized_tree)
            preorder(root.right, deserialized_tree)
    root = ser.deserialize(serialized_string)

    preorder(root, deserialized_tree)
    print(deserialized_tree)



