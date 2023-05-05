def remove_duplicates(a):
    j = 0
    element_dict = {}
    n = len(a)
    for i in range(0, n):
        if a[i] in element_dict:
            continue
        else:
            a[j] = a[i]
            element_dict[a[i]] = i
            j += 1
    a[j:] = ['_'] * (n-j)
    return j, a


if __name__ == "__main__":
    a = [1 ,1 , 2]
    print(remove_duplicates(a))
    a = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(remove_duplicates(a))