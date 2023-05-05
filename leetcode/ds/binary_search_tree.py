class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert_iter(self, val):
        if not self.root:
            self.root = Node(val)
            return
        parent, temp = self.root, self.root
        while temp:
            parent = temp
            if val < parent.val:
                temp = temp.left
                if temp is None:
                    parent.left = Node(val)
                    break
            elif val > parent.val:
                temp = temp.right
                if temp is None:
                    parent.right = Node(val)
                    break
            else:
                return
    def __insert_recur(self, root, val):
        if root:
            if val < root.val:
                if root.left:
                    self.__insert_recur(root.left, val)
                else:
                    root.left = Node(val)
            elif val > root.val:
                if root.right:
                    self.__insert_recur(root.right, val)
                else:
                    root.right = Node(val)
        else:
            self.root = Node(val)

    def insert(self, val):
        self.__insert_recur(self.root, val)

    def __remove_helper(self, root, val):
        if root:
            parent, temp = None, root
            while temp and val != temp.val:
                parent = temp
                if val < parent.val:
                    temp = temp.left
                elif val > parent.val:
                    temp = temp.right
            if temp is None:
                print(f'Node with value {val} is not found')
                return
            if temp.left is None or temp.right is None:
                new_succ = None
                if temp.left is None:
                    new_succ = temp.right
                else:
                    new_succ = temp.left
                if temp == parent.left:
                    parent.left = new_succ
                else:
                    parent.right = new_succ
                temp = None
                return
            else:
                new_parent = None
                new_temp = temp.right
                while new_temp.left:
                    new_parent = new_temp
                    new_temp = new_temp.left
                if new_parent:
                    new_parent.left = new_temp.right
                else:
                    temp.right = new_temp.right
                temp.val = new_temp.val
                temp = None

    def remove(self, val):
       self.__remove_helper(self.root, val)

    def inorder_traversal(self):
        visited = []
        self._inorder_traversal_helper(self.root, visited)
        return visited

    def _inorder_traversal_helper(self, root, visited):
        if root:
            self._inorder_traversal_helper(root.left, visited)
            visited.append(root.val)
            self._inorder_traversal_helper(root.right, visited)

    def preorder_traversal(self):
        visited = []
        self._preorder_traversal_helper(self.root, visited)
        return visited

    def _preorder_traversal_helper(self, root, visited):
        if root:
            visited.append(root.val)
            self._preorder_traversal_helper(root.left, visited)
            self._preorder_traversal_helper(root.right, visited)

    def postorder_traversal(self):
        visited = []
        self._postorder_traversal_helper(self.root, visited)
        return visited

    def _postorder_traversal_helper(self, root, visited):
        if root:
            self._postorder_traversal_helper(root.left, visited)
            self._postorder_traversal_helper(root.right, visited)
            visited.append(root.val)



if __name__=="__main__":
    bst = BinarySearchTree()
    for i in [7, 20, 5, 15, 10, 4, 4, 33, 2, 25, 6, 30]:
        bst.insert(i)
    print(bst.inorder_traversal())
    for i in [2, 15, 30, 7]:
        bst.remove(i)
        print(bst.inorder_traversal())
    bst.insert(7)
    bst.insert(8)
    print(bst.inorder_traversal())
    bst.remove(5)
    print(bst.inorder_traversal())
    print(bst.preorder_traversal())
    print(bst.postorder_traversal())


