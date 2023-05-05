def longest_substring_with_no_repeat_char(s):
    l = 0
    result = 0
    substring_set = set()
    for r in range(0, len(s)):
        while s[r] in substring_set:
            substring_set.remove(s[l])
            l += 1
        substring_set.add(s[r])
        result = max(result, r - l + 1)

    return result


if __name__ == "__main__":
    s = "abcabcbb"
    print(longest_substring_with_no_repeat_char(s))
    s = "bbbbba"
    print(longest_substring_with_no_repeat_char(s))
    s = "pwwkew"
    print(longest_substring_with_no_repeat_char(s))