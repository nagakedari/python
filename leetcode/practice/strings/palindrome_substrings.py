def is_palindrome(s):
    reversed_string = ''
    for i in range(len(s)-1, -1, -1):
        reversed_string += s[i]
    return s == reversed_string

def count_palindrome(s, l , r, n):
    res = 0
    while l >= 0 and r < n and s[l] == s[r]:
        res += 1
        l -= 1
        r += 1
    return res

def palindrome_substrings(s):
    res = 0
    n = len(s)
    for i in range(0, n):
        l = r = i
        res += count_palindrome(s, l, r, n)
        l = i
        r = i + 1
        res += count_palindrome(s, l, r, n)
    return res


if __name__=="__main__":
    s = "abc"
    print(palindrome_substrings(s))
    s = "aaa"
    print(palindrome_substrings(s))
    s = "aaabaaa"
    print(palindrome_substrings(s))