def is_palindrome(x):
    if x < 0:
        return False
    rev = 0
    original = x

    while x!=0:
        rev = rev * 10 + x % 10
        x //= 10
    return rev == original


if __name__=="__main__":
    print(is_palindrome(11211))