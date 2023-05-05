def max_sub_array_product(a):
    curr_min, curr_max, result = 1, 1, max(a)
    found_zero = False
    for i in range(0, len(a)):
        if a[i] == 0:
            curr_min, curr_max = 1, 1
            found_zero = True
            break
        temp = curr_max * a[i]
        curr_max = max(temp, curr_min * a[i], a[i])
        curr_min = min(temp, curr_min * a[i], a[i])
        result = max(result, curr_max)
    if found_zero:
        return max(result, 0)
    else:
         return result

if __name__ == "__main__":
    a = [2, 3, -2, 4]
    print(max_sub_array_product(a))
    a = [-2, 0, -1]
    print(max_sub_array_product(a))
    a = [-2, 3, -2, -4]
    print(max_sub_array_product(a))