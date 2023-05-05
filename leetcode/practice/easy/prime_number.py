def is_prime(num):
    if num == 0 or num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def list_prime_numbers(n):
    prime_list = []
    for i in range(1, n+1):
        if is_prime(i):
            prime_list.append(i)

    return prime_list

if __name__ == "__main__":
    print(is_prime(10))

    print(list_prime_numbers(10))