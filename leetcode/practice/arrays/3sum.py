
# O(n^2) my approach
def three_sum(a):
    ans = set()
    a_dict = {v: k for k, v in enumerate(a)}
    for i in range(0, len(a)):
        for j in range(0, len(a)):
            if i != j:
                sum = -(a[i] + a[j])
                if sum in a_dict:
                    if a_dict[sum] != j:
                        ans.add((a[a_dict[sum]], a[i], a[j]))
                        break

    if len(ans) == 0:
        print(f"The only possible triplet does not sum up to 0")
    else:
        print(list(set(map(tuple, map(sorted, ans)))))


def three_sum_better_approach(a):
    a = sorted(a)
    ans = set()
    for i in range(0, len(a)):
        left = i+1
        right = len(a) -1
        while (left < right):
            current_sum = a[i] + a[left] + a[right]
            if current_sum == 0:
                ans.add((a[i], a[left], a[right]))
                left += 1
                right -= 1
            elif current_sum > 0:
                right -= 1
            else:
                left += 1
    if len(ans) == 0:
        print(f"The only possible triplet does not sum up to 0")
    else:
        print(list(ans))


def three_sum_with_array(a):
    a.sort()
    ans = []
    n = len(a)
    for i in range(0, n):
        l = i+1
        r = n-1
        while (l < r):
            if [a[i], a[l], a[r]] in ans:
                break
            curr_sum = a[i] + a[l] + a[r]
            if curr_sum == 0:
                ans.append([a[i], a[l], a[r]])
                l += 1
                r -= 1
            elif curr_sum < 0:
                l += 1
            else:
                r -=1
    if len(ans) == 0:
        print(f"The only possible triplet does not sum up to 0")
    else:
        print(list(ans))


if __name__ == "__main__":
    a = [-1, 0, 1, 2, -1, -4]
    # three_sum_better_approach(a)
    three_sum_with_array(a)
    a = [0, 1, 1]
    # three_sum_better_approach(a)
    three_sum_with_array(a)
    a = [0, 0, 0]
    # three_sum_better_approach(a)
    three_sum_with_array(a)