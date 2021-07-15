class Heap:
    def __init__(self):
        self.arr = []
    def insert(self, val):
        self.arr.append(val)
        current_heap_size = len(self.arr)
        i = int((current_heap_size / 2)-1)
        for i in range(current_heap_size, -1, -1):
            self.max_hepify(self.arr,i,current_heap_size)
    def max_hepify(self, a, i , current_heap_size):
        left = 2 * i  + 1
        right = 2 * i + 2
        largest = i

        if left < current_heap_size and a[i] < a[left] :
            largest = left

        if right < current_heap_size and a[i] < a[right] :
            largest = right

        if largest != i:
            a[i], a[largest] = a[largest], a[i]
            self.max_hepify(a, largest, current_heap_size)

    def print_heap(self):
        print(self.arr)
    
    def sort(self):
        for i in range(len(self.arr)-1, 0, -1):
            self.arr[i], self.arr[0] = self.arr[0], self.arr[i]
            self.max_hepify(self.arr, 0, i-1)
heap = Heap()
heap.insert(10)
heap.insert(30)
heap.insert(40)
heap.insert(15)
heap.insert(50)
heap.insert(100)
heap.insert(70)

heap.print_heap()

heap.sort()

heap.print_heap()
