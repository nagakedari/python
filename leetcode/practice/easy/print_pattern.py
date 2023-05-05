def print_pattern(n):
    for i in range(0, n):
        print('*' * (i+1))
    print("\n")
    for i in range(0, n):
        print(' ' * (n-i-1), "*" * (i+1))
    print("\n")
    for i in range(n-1, -1, -1):
        print('*' * (i+1))
    print("\n")
    k = n - 1
    for i in range(0, n):
        print(end=" " * k)
        k -= 1
        print('* ' * (i+1), " ")

if __name__=="__main__":
    print_pattern(5)