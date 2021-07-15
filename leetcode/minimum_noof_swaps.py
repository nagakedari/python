def find_minimum_swaps(arr):
    temp = arr.copy()
    temp.sort()
    noof_swaps = 0
    h = {}
    for index, arr_val in enumerate(arr):
        h[arr_val] = index
    for i in range(len(arr)):
        if arr[i] != temp[i]:
            init = arr[i]
            index = h[temp[i]]
            arr[i], arr[index] = arr[index], arr[i]
            h[init], h[temp[i]] = h[temp[i]], i
            noof_swaps+= 1
    return noof_swaps

def find_index(a, value):
    for index, arr_val in enumerate(a):
        if arr_val== value:
            return index
print(find_minimum_swaps([101, 758, 315, 730, 472, 619, 460, 479]))