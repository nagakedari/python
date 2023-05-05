def max_profit(a):
    i = 0
    j = len(a) -1
    min = a[i]
    max = a[j]
    while i < j:
        if a[i] < min:
            min = a[i]
        if a[j] > max:
            max = a[j]
        i += 1
        j -= 1
    profit = (max - min)
    if profit > 0:
        return profit
    else:
        return 0

# Approach 2
def max_profit_1(a):
    i = 0
    minimum = a[i]
    max_profit = 0
    for i in range(0, len(a)):
        # if a[i] < min:
        #     min = a[i]
        minimum = min(a[i], minimum)
        max_profit = max(max_profit, a[i]-minimum)
    return max_profit


if __name__ == "__main__":
    a = [7, 1, 5, 3, 6, 4]
    # a = [7,6,4,3,1]
    print(max_profit(a))
    print(max_profit_1(a))
