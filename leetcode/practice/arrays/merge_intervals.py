def merge_inervals(a):
    a = sorted(a)
    prev_i = a[0]
    ans = []
    for i in range(1, len(a)):
        i_interval = a[i]
        if i_interval[0] <= prev_i[1]:
            if prev_i[1] <= i_interval[1]:
                prev_i = [prev_i[0], i_interval[1]]
        else:
            ans.append(prev_i)
            prev_i = i_interval
    ans.append(prev_i)
    return ans

def merge_inervals_2nd(a):
    a = sorted(a)
    temp = a[0]
    ans = []
    for i in range(1, len(a)):
        i_interval = a[i]
        if temp[1] >= i_interval[0]:
            if temp[1] <= i_interval[1]:
                temp = [temp[0], i_interval[1]]
        else:
            ans.append(temp)
            temp = i_interval
    ans.append(temp)
    return ans

if __name__ == "__main__":
    a = [[1, 3], [2, 6], [15, 18], [8, 10]]
    print(merge_inervals(a))
    print(merge_inervals_2nd(a))
    a = [[1, 4], [4, 5]]
    print(merge_inervals(a))
    print(merge_inervals_2nd(a))
    a = [[1, 3], [2, 6], [4, 5], [6,10], [12, 15]]
    print(merge_inervals(a))
    print(merge_inervals_2nd(a))
    a = [[1, 3], [2, 6], [4, 5], [6, 10], [7, 15]]
    print(merge_inervals(a))
    print(merge_inervals_2nd(a))