class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, node):
        if self.root:
            parent = self.root
            while parent:
                temp = parent
                if node.value <= parent.value:
                    parent = parent.left
                else:
                    parent = parent.right
            if node.value <= temp.value:
                temp.left = node
            else:
                temp.right = node
        else:
            self.root = node
    def __inrder_traversal_helper(self, root, visited):
        if root:
            self.__inrder_traversal_helper(root.left, visited)
            visited.append(root.value)
            self.__inrder_traversal_helper(root.right, visited)

    def traversal(self):
        visited = []
        self.__inrder_traversal_helper(self.root, visited)
        return visited
    
    def inorder_traversal(self,node):
        if node == None:
            return
        self.inorder_traversal(node.left)
        print(node.value, end=" ")
        self.inorder_traversal(node.right)
    def preorder_traversal(self,node):
        if node == None:
            return
        print(node.value, end=" ")
        self.preorder_traversal(node.left)
        self.preorder_traversal(node.right)
    def postorder_traversal(self,node):
        if node == None:
            return
        self.postorder_traversal(node.left)
        self.postorder_traversal(node.right)
        print(node.value, end=" ")

    def levelorder_traversal(self, node):
        height_of_the_tree = self.hieght()
        for i in range(height_of_the_tree + 1):
            self.printNodesAtGivenLevel(node, i)

    def printNodesAtGivenLevel(self, node, level):
        if node is None:
            return
        if level == 0:
            print(node.value, end=" ")
        elif level >= 0:
            self.printNodesAtGivenLevel(node.left, level-1)
            self.printNodesAtGivenLevel(node.right, level-1)
    
    def levelorder_reversal_traversal(self, node):
        no_of_levels = self.hieght()+1
        while no_of_levels > 0:
            self.printNodesUntilTheGivenLevel(node, 1, no_of_levels)
            no_of_levels-=1

    def printNodesUntilTheGivenLevel(self, node, level, no_of_levels):
        if node is None:
            return
        if level == no_of_levels:
            print(node.value, end=" ")
        elif level < no_of_levels:
            self.printNodesUntilTheGivenLevel(node.left, level+1,no_of_levels)
            self.printNodesUntilTheGivenLevel(node.right, level+1,no_of_levels)
        
         
    def insert_recurr(self, node):
        self.insert_recurr_helper(self.root, node)
    
    def insert_recurr_helper(self, current, node):
        if current:
            if node.value < current.value:
                if current.left:
                    self.insert_recurr_helper(current.left, node)
                else:
                    current.left = node
            else:
                if current.right:
                    self.insert_recurr_helper(current.right, node)
                else:
                    current.right = node
        else:
            self.root = node
    def search(self, key):
        return self.search_recurr(self.root, key)

    def search_recurr(self, current, key):
        if current:
            if key == current.value:
                return True
            elif key < current.value:
                return self.search_recurr(current.left, key)
            else:
                return self.search_recurr(current.right, key)
        return False

    def delete(self, key):
        curr = self.root
        prev = None

        while (curr != None and curr.value != key):
            prev = curr
            if key < curr.value:
                curr = curr.left
            else:
                curr = curr.right
            
        if curr.left == None or curr.right == None:
            new_curr = None
            if curr.left == None:
                new_curr = curr.right
            else:
                new_curr = curr.left

            if prev == None:
                return new_curr
                
            if curr == prev.left:
                prev.left =  new_curr
            else:
                prev.right = new_curr
            curr = None
        else:
            p = None
            temp = None
            temp = curr.right 
            while(temp.left != None): 
                p = temp 
                temp = temp.left 
            if p != None: 
                p.left = temp.right 
            else: 
                curr.right = temp.right 
            curr.data = temp.data 
            temp = None
        return self.root

    def __remove_helper(self, root, val):
        if root:
            parent, temp = None, root
            while temp and val != temp.value:
                parent = temp
                if val < parent.value:
                    temp = temp.left
                elif val > parent.value:
                    temp = temp.right
            if temp is None:
                print(f"Node with value {val} is not found")
                return
            if temp.left is None or temp.right is None:
                if temp.left is None:
                    if temp.value < parent.value:
                        parent.left = temp.right
                    else:
                        parent.right = temp.right
                elif temp.right is None:
                    if temp.value > parent.value:
                        parent.right = temp.left
                    else:
                        parent.left = temp.left
                temp = None
                return
            else:
                new_temp = temp.right
                while new_temp.left:
                    new_temp = new_temp.left
                temp.val = new_temp.value
                self.__remove_helper(temp.right, new_temp.value)

    
    def remove(self, val):
        self.__remove_helper(self.root, val)

    def hieght(self):
        return self.height_helper(self.root)
    
    def height_helper(self, root):
        if root is None:
            return -1

        hleft= self.height_helper(root.left) 
        hright= self.height_helper(root.right)

        if hleft > hright:
            return hleft+1
        else:
            return hright+1

    def vertical_traversal(self, root):
        # self.vertical_traversal_helper(root, horizontal_distance_from_the_root)
        nodes_hd_map = dict()
        self.vertical_traversal_helper(root, 0,nodes_hd_map)
        for i in nodes_hd_map:
            print('{} - {}'.format(i, nodes_hd_map[i]))
    
    def vertical_traversal_helper(self, node, hd, n_hd_map):
        if node is None:
            return
        try:
            n_hd_map[hd].append(node.value)
        except:
            n_hd_map[hd] = [node.value]
        self.vertical_traversal_helper(node.left, hd-1, n_hd_map)
        self.vertical_traversal_helper(node.right, hd+1, n_hd_map)
    
tree = BinarySearchTree()
for i in [7, 20, 5, 15, 10, 4, 33, 2, 25, 6, 30]:
    node = Node(i)
    tree.insert_recurr(node)
print(tree.traversal())
for i in [2, 15, 30, 7, 5]:
    tree.remove(i)
    print(tree.traversal())

# root = Node(7)
# node1 = Node(5)
# node2 = Node(20)
# node3 = Node(6)
# node4 = Node(15)
# node5 = Node(8)
# node6 = Node(16)
# node7 = Node(25)
# node8 = Node(3)
# node9 = Node(1)
# node10 = Node(4)

# tree.insert(root)
# tree.insert(node1)
# tree.insert(node2)
# tree.insert(node3)
# tree.insert(node4)
# tree.insert(node5)
# tree.insert(node6)
# tree.insert(node7)
# tree.insert(node8)
# tree.insert(node9)
# tree.insert(node10)

# tree.insert_recurr(root)
# tree.insert_recurr(node1)
# tree.insert_recurr(node2)
# tree.insert_recurr(node3)
# tree.insert_recurr(node4)
# tree.insert_recurr(node5)
# tree.insert_recurr(node6)
# tree.insert_recurr(node7)
# tree.insert_recurr(node8)
# tree.insert_recurr(node9)
# tree.insert_recurr(node10)

# tree.inorder_traversal(root)

# print("\n")
# print('The tree has the value:{} : {}'.format(3, tree.search(3)))
# print('The tree has the value:{} : {}'.format(17, tree.search(17)))
# tree.insert_recurr(Node(17))
# print(tree.hieght())
# tree.preorder_traversal(root)
# print("\n")
# tree.postorder_traversal(root)
# print("\n")
# tree.levelorder_traversal(root)
# print("\n")
# tree.levelorder_reversal_traversal(root)
# tree.delete(3)
# tree.vertical_traversal(root)