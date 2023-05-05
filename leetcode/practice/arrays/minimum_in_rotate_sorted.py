def min_in_rotated_sorted(a):
    n = len(a)
    l = 0
    r = n - 1
    min_value = a[l]
    while l <= r:
        if a[l] < a[r]:
            return a[l]
        m = int((l + r) / 2)
        min_value = min(min_value, a[m])
        if a[m] < a[r]:
            r = m - 1
        else:
            l = m + 1
    return min_value


if __name__ == "__main__":
    a = [7, 0, 1, 2, 4, 5, 6]
    print(min_in_rotated_sorted(a))
    a = [3, 4, 5, 1, 2]
    print(min_in_rotated_sorted(a))
    a = [11, 13, 15, 17]
    print(min_in_rotated_sorted(a))