def find_mex(a):
    min_v = min(a)
    max_v = max(a)
    temp_arr = []
    for i in range(min_v, max_v+1):
        temp_arr.append(i)
    for i in temp_arr:
        exists=False
        for j in a:
            if i == j:
                exists=True
        if not exists:
            return i
# print(find_mex([1,0,3]))
print(find_mex([1,0]))
# print(find_mex([9, 0, 3, 5, 7, 2, 4, 1, 10, 19]))

def eqal_MEX(n, a):
    if n > 2:
        mid = int(n/2)
        sub1 = a[0:mid]
        sub2 = a[mid:n]
        sub1_mex = find_mex(sub1)
        sub2_mex = find_mex(sub2)
        