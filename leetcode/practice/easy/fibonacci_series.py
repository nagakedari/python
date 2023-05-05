def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


def fibonacci_series(n):
    fib_s = []
    for i in range(n):
        if i == 0 or i == 1:
            fib_s.append(i)
        else:
            fib_s.append(fib_s[i-1] + fib_s[i-2])
    return fib_s

if __name__ == "__main__":
    series = [fibonacci(i) for i in range(15)]
    print(series)

    print(fibonacci_series(15))