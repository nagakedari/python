class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
    def insert_first(self, new_item):
        new_item.next = self.head
        self.head = new_item
    def delete_first(self):
        if self.head:
            first = self.head
            self.head = first.next
            first.next = None
            return first
        else:
            return None
class Stack():
    def __init__(self, top=None):
        self.ll = LinkedList(top)
    def push(self, new_item):
        self.ll.insert_first(new_item)
    def pop(self):
        return self.ll.delete_first()
            
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)
stack.push(e3)
print(stack.pop().value)
print(stack.pop().value)
print(stack.pop().value)
print(stack.pop())
stack.push(e4)
print(stack.pop().value)