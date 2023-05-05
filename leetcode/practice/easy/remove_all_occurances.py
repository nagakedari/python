def remove_all_occurance(a, val):
    j = 0
    n = len(a)

    for i in range(0, n):
        if a[i] == val:
            continue
        else:
            a[j] = a[i]
            j += 1
    a[j:] = ['_'] * (n-j)

    return j, a


if __name__ == "__main__":
    a = [3, 2, 2, 3]
    print(remove_all_occurance(a, 3))
    a = [0,1,2,2,3,0,4,2]
    print(remove_all_occurance(a, 2))
