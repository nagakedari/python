def quick_sort(a, l, r):
    if l < r:
        pivot = partition(a, l, r)
        quick_sort(a, l, pivot-1)
        quick_sort(a, pivot+1, r)
    

def partition(a, l , r):
    pivot = r
    i = 0
    while i < pivot:
        if a[i] > a[pivot]:
            temp = a[pivot]
            a[pivot] = a[i]
            pivot -=1
            a[i] = a[pivot]
            a[pivot] = temp
        else:
            i += 1
    return pivot
            
test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
quick_sort(test, 0, len(test)-1)
print('quick sorted array: {}'.format(test))