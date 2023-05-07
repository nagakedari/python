def _heapify(a, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and a[l] > a[largest]:
        largest = l

    if r < n and a[r] > a[largest]:
        largest = r
    
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        _heapify(a, n, largest)


if __name__ == "__main__":
    a = [5, 4, 2, 10, 3, 1, 0]
    n = len(a)
    for i in range(n//2 -1, -1, -1):
        _heapify(a, n, i)
    for i in range(n - 1, 0, -1):
        (a[i], a[0]) = (a[0], a[i])  # swap
        _heapify(a, i, 0)
    print(a)