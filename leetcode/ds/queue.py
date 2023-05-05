class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, data):
        new_elem = Node(data)
        if not self.head and not self.tail:
            self.head = new_elem
            self.tail = new_elem
        else:
            self.tail.next = new_elem
            self.tail = new_elem
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            print("queue is empty")
            return
        self.head = self.head.next

    def print(self):
        queue_elements = []
        if not self.head:
            print("queue is empty")
            return
        trav = self.head
        while trav:
            queue_elements.append(str(trav.data))
            trav = trav.next
        print(f"head --> {'-->'.join(queue_elements)} <--tail")


class QueueWithArray:
    def __init__(self):
        self.f = self.r = 0
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)
        self.r += 1

    def dequeue(self):
        self.queue.pop(0)
        self.r -= 1

    def print(self):
        print(self.queue)

if __name__ == "__main__":
    # q = Queue()
    # q.enqueue(2)
    # q.enqueue(3)
    # q.enqueue(4)
    # q.enqueue(5)
    # q.enqueue(6)
    # q.enqueue(7)
    #
    # q.print()
    #
    # q.dequeue()
    # q.dequeue()
    # q.dequeue()
    # q.dequeue()
    # q.dequeue()
    #
    # q.print()

    q = QueueWithArray()
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(7)

    q.print()

    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()

    q.print()


