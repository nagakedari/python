class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.size = 0

    def _hepify(self, i):
        l = 2*i + 1
        r = 2*i + 2
        smallest = i
        if l < self.size and self.queue[smallest] > self.queue[l]:
            smallest = l
        if r < self.size and self.queue[smallest] > self.queue[r]:
            smallest = r
        if smallest != i:
            self.queue[i], self.queue[smallest] = self.queue[smallest], self.queue[i]
            self._hepify(smallest)

    def add(self, data):
        self.queue.append(data)
        self.size += 1
        for i in range((self.size)//2 -1, -1, -1):
            self._hepify(i)

    def _remove_at(self, index):
        self.queue[index], self.queue[-1] = self.queue[-1], self.queue[index]
        self.queue.pop(-1)
        self.size -= 1
        self._hepify(index)

    def remove(self, data):
        remove_index = None
        for i in range(0, self.size):
            if self.queue[i] == data:
                remove_index = i
                break
        if remove_index:
            self._remove_at(remove_index)
        else:
            print("queue doesn't have the element")

    def poll(self):
        self._remove_at(0)

    def print(self):
        print(self.queue)


if __name__ == "__main__":
    priority_q = PriorityQueue()
    priority_q.add(1)
    priority_q.add(5)
    priority_q.add(6)
    priority_q.add(8)
    priority_q.add(12)
    priority_q.add(13)
    priority_q.add(11)
    priority_q.add(7)
    priority_q.add(1)
    priority_q.add(2)
    priority_q.add(2)
    priority_q.add(2)
    priority_q.add(15)
    priority_q.add(3)
    priority_q.add(10)
    priority_q.print()
    priority_q.poll()
    priority_q.print()
    priority_q.remove(6)
    priority_q.print()
    priority_q.remove(5)
    priority_q.print()



