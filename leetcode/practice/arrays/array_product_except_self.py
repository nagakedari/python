# division approach
def product_except_self(a):
    total_product = 1
    product_except_0 = 1
    zero_count = 0
    for i in range(0, len(a)):
        total_product *= a[i]
        if a[i] == 0 and zero_count < 1:
            zero_count += 1
        else:
            product_except_0 *= a[i]

    ans = []
    for i in range(0, len(a)):
        if a[i] == 0:
            if zero_count > 1:
                ans.append(0)
            else:
                ans.append(product_except_0)
        else:
            ans.append(int(total_product/a[i]))
    return ans

# O(n^2)
def product_except_self_n_square(a):
    ans = []
    for i in range(0, len(a)):
        product = 1
        for j in range(0, len(a)):
            if i == j:
                continue
            product *= a[j]
        ans.append(product)
    return ans


# O(n)
def product_except_self_better_approach(a):
    prefix = 1
    n = len(a)
    ans = [1] * n
    postfix = 1
    for i in range(1, n):
        ans[i] = prefix * a[i-1]
        prefix *= a[i-1]
    for i in range(n-1, -1, -1):
        ans[i] *= postfix
        postfix *= a[i]
    return ans

def product_except_self_single_pass(a):
    prefix = 1
    n = len(a)
    ans = [1] * n
    postfix = 1
    for i in range(0, n):
        ans[i] *= prefix
        prefix *= a[i]
        ans[n-i-1] *= postfix
        postfix *= a[n-i-1]
    return ans

if __name__ == "__main__":
    a = [1, 2, 3, 4]
    # a = [-1, 1, 0, -3, -4]
    # print(product_except_self(a))
    # print(product_except_self_n_square(a))
    print(product_except_self_better_approach(a))
    print(product_except_self_single_pass(a))