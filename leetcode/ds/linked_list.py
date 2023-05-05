class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None


class DNode:

    def __init__(self,data=None):
        self.data = data
        self.next = None
        self.previous = None


class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, data):
        if self.head:
            traverser = self.head
            while traverser.next:
                traverser = traverser.next
            traverser.next = Node(data)
        else:
            self.head = Node(data)
        self.size += 1

    def add_at(self, index, data):
        if index > self.size+1:
            print("Linked List doesn't have those many elements and hence it cannot add at the given index")
            return
        if self.head:
            count = 1
            traverser = self.head
            next_traverser = traverser.next
            if count == index:
                new_node = Node(data)
                new_node.next = traverser
                self.head = new_node
                return
            while next_traverser and count+1 < index:
                traverser = traverser.next
                next_traverser = next_traverser.next
                count += 1

            new_node = Node(data)
            new_node.next = next_traverser
            traverser.next = new_node
        else:
            self.head = Node(data)
        self.size += 1

    def remove(self, data):
        if self.size == 0:
            print("Linked List is empty")
            return

        traverser = self.head
        traverser_next = traverser.next
        if self.head.data == data:
            self.head = traverser_next
            self.size -= 1
            return
        else:
            while traverser_next:
                if traverser_next.data == data:
                    traverser.next = traverser_next.next
                    break
                else:
                    traverser = traverser_next
                    traverser_next = traverser_next.next
            self.size -= 1

    def print(self):
        if not self.head:
            print([])
            return
        nodes = [str(self.head.data)]
        traverser = self.head
        while traverser.next:
            traverser = traverser.next
            nodes.append(str(traverser.data))

        print(f"Linked List: {'--->'.join(nodes)}")

    def len(self):
        return self.size

    def reverse_list(self):
        if self.head:
            prev = None
            current = self.head
            while current:
                next = current.next
                current.next = prev
                prev = current
                current = next
            self.head = prev
            self.print()
        else:
            self.print()





class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.next = None
        self.previous = None
        self.size = 0

    def insert(self, data):
        if not self.head:
            new_node = DNode(data)
            self.head = new_node
            self.size += 1
            return
        else:
            trav = self.head
            while trav.next:
                trav = trav.next
            new_node = DNode(data)
            new_node.next = trav.next
            new_node.previous = trav
            trav.next = new_node
            self.size += 1

    def insert_at(self, index, data):
        if index > self.size + 1:
            print("Doubly Linked List doesn't have those many elements and hence it cannot add at the given index")
            return
        if not self.head:
            new_node = DNode(data)
            self.head = new_node
            self.size += 1
            return
        count = 1
        trav = self.head

        for i in range(0, index):
            trav = trav.next
        # if count == index:
        new_node = DNode(data)
        new_node.next = trav
        trav.next.previous = new_node
        self.size += 1
        # if count == 1:
        #     self.head = new_node


    def remove(self, data):
        if not self.head:
            print('Doubly linked list is empty')
            return
        trav = self.head
        if self.head.data == data:
            self.head = self.head.next
            if self.head:
                self.head.previous = None
            self.size -= 1
            return
        while trav.next:
            if trav.data == data:
                prev_node = trav.previous
                prev_node.next = trav.next
                trav.next.previous = prev_node
                self.size -= 1
                return
            else:
                trav = trav.next

    def print(self):
        if not self.head:
            print([])
            return
        nodes = [str(self.head.data)]
        traverser = self.head
        while traverser.next:
            traverser = traverser.next
            nodes.append(str(traverser.data))

        print(f"Doubly Linked List: {'<--->'.join(nodes)}")

    def len(self):
        return self.size


def has_cycle(head):
    node_visited_dict = {}
    current = head
    while current:
        if current in node_visited_dict:
            return True
        else:
            node_visited_dict[current] = current
            current = current.next

    return False

def has_cycle_floyds_tortois_approach(head):
    s_p = head
    f_p = head
    while f_p and f_p.next:
        f_p = f_p.next.next
        s_p = s_p.next
        if s_p == f_p:
            return True
    return False

if __name__ == "__main__":
    # dlist = DoublyLinkedList()
    # print(f"linked list size: {dlist.len()}")
    # dlist.insert(12)
    # print(f"linked list size: {dlist.len()}")
    # dlist.insert(24)
    # print(f"linked list size: {dlist.len()}")
    # dlist.insert(36)
    # print(f"linked list size: {dlist.len()}")
    # # dlist.insert_at(2, 48)
    # print(f"linked list size: {dlist.len()}")
    # dlist.print()
    # dlist.remove(24)
    # print(f"linked list size: {dlist.len()}")
    # dlist.print()
    # dlist.remove(48)
    # print(f"linked list size: {dlist.len()}")
    # dlist.remove(12)
    # print(f"linked list size: {dlist.len()}")
    # dlist.remove(36)
    # dlist.print()
    # print(f"linked list size: {dlist.len()}")
    # singly_list = SinglyLinkedList()
    # print(f"linked list size: {singly_list.len()}")
    # singly_list.add(12)
    # print(f"linked list size: {singly_list.len()}")
    # singly_list.add(24)
    # print(f"linked list size: {singly_list.len()}")
    # singly_list.add(36)
    # print(f"linked list size: {singly_list.len()}")
    # singly_list.add_at(4, 48)
    # print(f"linked list size: {singly_list.len()}")
    # singly_list.print()
    # singly_list.remove(24)
    # print(f"linked list size: {singly_list.len()}")
    # singly_list.print()
    # singly_list.remove(48)
    # print(f"linked list size: {singly_list.len()}")
    # singly_list.remove(12)
    # print(f"linked list size: {singly_list.len()}")
    # singly_list.remove(36)
    # singly_list.print()
    # print(f"linked list size: {singly_list.len()}")
    # singly_list = SinglyLinkedList()
    # singly_list.add(1)
    # singly_list.add(2)
    # singly_list.add(3)
    # singly_list.add(4)
    # singly_list.add(5)
    # singly_list.reverse_list()
    #
    # singly_list = SinglyLinkedList()
    # singly_list.add(1)
    # singly_list.add(2)
    # singly_list.reverse_list()
    #
    # singly_list = SinglyLinkedList()
    # singly_list.reverse_list()

    head = Node(3)
    head.next = Node(2)
    head.next.next = Node(0)
    head.next.next.next = Node(-4)
    # head.next.next.next.next = head.next
    print(has_cycle(head))
    print(has_cycle_floyds_tortois_approach(head))




