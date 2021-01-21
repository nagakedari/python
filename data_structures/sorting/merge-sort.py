def merge_sort(a):
    length = len(a)
    if length > 1 :
        mid = int(length/2)
        left = a[:mid]
        right = a[mid:]

        merge_sort(left)
        merge_sort(right)
        
        i = j = k = 0
        left_l = len(left)
        right_l = len(right)
        while i < left_l and j < right_l:
            if right[j]> left[i]:
                a[k] = left[i]
                i+=1
            else:
                a[k] = right[j]
                j+=1
            k+=1
        while i< left_l:
            a[k] = left[i]
            k+=1
            i+=1
        while j < right_l:
            a[k] = right[j]
            k+=1
            j+=1
           
        return a
    else:
        return a


print('Merge Sorted Array {}'.format(merge_sort([1,4,8,3,6,2,10,12,11,23])))


