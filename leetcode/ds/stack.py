class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        if self.top:
            node.next = self.top
        self.top = node

    def pop(self):
        if not self.top:
            print("stack is empty")
            return
        self.top = self.top.next

    def print(self):
        stack_elements = []
        if not self.top:
            print("stack is empty")
            return
        trav = self.top
        while trav:
            stack_elements.append(str(trav.data))
            trav = trav.next
        print(f"top --> {'-->'.join(stack_elements)}")


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(10)
    stack.print()
    stack.pop()
    stack.pop()
    stack.print()
