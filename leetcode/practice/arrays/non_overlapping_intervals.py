def non_overlapping_intervals(a):
    count = 0
    a = sorted(a)
    prev_end = a[0][1]
    for start, end in a[1:]:
        if prev_end > start:
            count += 1
            prev_end = min(end, prev_end)
        else:
            prev_end = end
    return count


if __name__ == "__main__":
    a = [[1, 2], [2, 3], [3, 4], [1, 3]]
    print(non_overlapping_intervals(a))
    a = [[1, 2], [1, 2], [1, 2]]
    print(non_overlapping_intervals(a))
    a = [[1, 2], [2, 3]]
    print(non_overlapping_intervals(a))