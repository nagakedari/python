
def max_subarray_sum(a):
    for i in range(1, len(a)):
        if a[i-1] > 0:
            a[i] += a[i-1]
    return max(a)


def max_subarray_sum_my_approach(a):
    temp = 0
    max_sum = a[0]
    for i in range(0, len(a)):
        temp += a[i]
        if temp > max_sum:
            max_sum = temp
        if temp < 0:
            temp = 0

    return max_sum


if __name__ == "__main__":
    a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # print(max_subarray_sum(a))
    print(max_subarray_sum_my_approach(a))
    print(max_subarray_sum_my_approach(a))