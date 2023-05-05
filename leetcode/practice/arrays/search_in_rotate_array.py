def search_in_rotated_array(a, target):
    l, r = 0, len(a)-1
    while (l <= r):
        m = int((l+r)/2)
        if target == a[m]:
            return m
        if a[l] <= a[m]:
            if target > a[m] or target < a[l]:
                l = m + 1
            else:
                r = m -1
        else:
            if target < a[m] or target > a[r]:
                r = m-1
            else:
                l = m+1
    return -1

def search_in_rotate_recursive(a,l,r,target):
    if l > r:
        return -1
    m = int((l+r)/2)

    if a[m] == target:
        return m
    elif a[l] <= a[m]:
        if target < a[l] or target > a[m]:
            return search_in_rotate_recursive(a, m+1, r, target)
        else:
            return search_in_rotate_recursive(a, l, m-1, target)
    else:
        if target > a[r] or target < a[m]:
            return search_in_rotate_recursive(a, l, m-1, target)
        else:
            return search_in_rotate_recursive(a, m+1, r, target)




if __name__ == "__main__":
    a = [4,5,6,7,0,1,2]
    result = search_in_rotated_array(a, 0)
    print(result)
    result = search_in_rotate_recursive(a,0,len(a)-1, 0)
    print(result)
    result = search_in_rotated_array(a, 3)
    print(result)
    result = search_in_rotate_recursive(a,0,len(a)-1,3)
    print(result)
    result = search_in_rotated_array(a, 6)
    print(result)
    result = search_in_rotate_recursive(a, 0, len(a) - 1, 6)
    print(result)