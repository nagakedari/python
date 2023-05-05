def _heapify(a, i, n):
    l = 2*i+1
    r = 2*i+2
    smallest = i
    if l < n and a[smallest] > a[l]:
        smallest = l
    if r < n and a[smallest] > a[r]:
        smallest = r

    if i != smallest:
        # swap
        a[i], a[smallest] = a[smallest], a[i]
        _heapify(a, smallest, n)


if __name__ == "__main__":
    a = [5, 4, 2, 10, 3, 1, 0]
    n = len(a)
    for i in range(int(n/2) - 1, -1, -1):
        _heapify(a, i, n)
    for i in range(n-1, 0, -1):
        a[i], a[0] = a[0], a[i]
        _heapify(a, 0, i)
    print(a)