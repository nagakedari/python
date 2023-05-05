def container_max_water_brute_force(a):
    n = len(a)
    max_area = 1
    for i in range(0,n):
        for j in range(i+1, n):
            w = j - i
            h = min (a[i], a[j])
            max_area = max(max_area, w*h)
    return max_area

def container_max_water(a):
    n = len(a)
    max_area = 1
    l = 0
    r = n-1
    while l < r :
        w = r - l
        h = min(a[l], a[r])
        max_area = max(max_area, w * h)
        if a[l] < a[r]:
            l = l + 1
        else:
            r = r - 1

    return max_area


if __name__=="__main__":
    a = [1, 8, 6, 2, 5, 4 ,8, 3, 7]
    print(container_max_water_brute_force(a))
    a = [1, 1]
    print(container_max_water_brute_force(a))
    a = [1, 8, 10, 2, 5, 9, 8, 3, 7, 8]
    print(container_max_water(a))
    a = [1, 1]
    print(container_max_water(a))