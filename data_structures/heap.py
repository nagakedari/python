class Heap:
    def __init__(self):
        self.arr = []
    def insert(self, val):
        self.arr.append(val)
        current_heap_size = len(self.arr)
        if current_heap_size > 1:
            i = int(current_heap_size / 2)-1
            while i >= 1:
                self.max_hepify(self.arr, i, current_heap_size)
                i-= 1
    def max_hepify(self, a, i , current_heap_size):
        left = 2 * i 
        right = 2 * i + 1
        largest = i

        if left < current_heap_size and a[i] < a[left] :
            largest = left

        if right < current_heap_size and a[i] < a[right] :
            largest = right

        if largest != i:
            self.swap(a, i, largest)
            self.max_hepify(a, largest, current_heap_size)

    def swap (self, a, i, j):
        temp = a[i]
        a[i] = a[j]
        a[j] = temp

    def print_heap(self):
        print(self.arr)

heap = Heap()
heap.insert(10)
heap.insert(30)
heap.insert(40)
heap.insert(15)
heap.insert(50)
heap.insert(100)
heap.insert(70)

heap.print_heap()
