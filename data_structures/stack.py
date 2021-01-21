class Stack():
    def __init__(self):
        self.stack = []
        self.top = -1
    
    def push(self, value):
        self.top+=1
        self.stack.append(value)

    def pop(self):
        del self.stack[self.top]
        self.top-=1

    def print_stack(self):
        top_index = self.top
        while top_index >= 0:
            print(self.stack[top_index])
            top_index-=1

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

stack.print_stack()

stack.pop()

stack.print_stack()

