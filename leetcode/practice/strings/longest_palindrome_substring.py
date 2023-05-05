def current_max_palindrome(s, l, r, n, result,  longest_pali_len):
    while l >= 0 and r < n and s[l] == s[r]:
        if (r - l + 1) > longest_pali_len:
            result = s[l:r + 1]
            longest_pali_len = r - l + 1
        l -= 1
        r += 1
    return result, longest_pali_len

def longest_palindrome_substring(s):
    n = len(s)
    result = ''
    longest_pali_len = 0
    for i in range(0, n):
        # l = r = i
        result, longest_pali_len = current_max_palindrome(s, i, i, n, result, longest_pali_len)
        # l = i
        # r = i + 1
        result, longest_pali_len = current_max_palindrome(s, i, i+1, n, result, longest_pali_len)
        # if len(even_palindrome) > len(odd_palindrome):
        #     temp = even_palindrome
        # else:
        #     temp = odd_palindrome
        # if len(temp) > len(result):
        #     result = temp

    return result


if __name__=="__main__":
    s = "babad"
    print(longest_palindrome_substring(s))
    s = "cbbd"
    print(longest_palindrome_substring(s))
    s = "aaabaaa"
    print(longest_palindrome_substring(s))