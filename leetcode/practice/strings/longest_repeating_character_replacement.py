def longest_repeating_character_replacement(s, k):
    char_freq_map = dict()
    l = 0
    result = 0
    for r in range(0, len(s)):
        if s[r] in char_freq_map:
            char_freq_map[s[r]] += 1
        else:
            char_freq_map[s[r]] = 1
        curr_window_size = r - l + 1
        if (curr_window_size - max(char_freq_map.values())) <= k:
            result = max(result, curr_window_size)
            r += 1
        else:
            char_freq_map[s[l]] -= 1
            l += 1
    return result


def longest_repeating_character_replacement_optimized(s, k):
    char_freq_map = dict()
    l = 0
    result = 0
    max_freq = 0
    for r in range(0, len(s)):
        if s[r] in char_freq_map:
            char_freq_map[s[r]] += 1
        else:
            char_freq_map[s[r]] = 1
        max_freq = max(max_freq, char_freq_map[s[r]])
        curr_window_size = r - l + 1
        if (curr_window_size - max_freq) <= k:
            result = max(result, curr_window_size)
            r += 1
        else:
            char_freq_map[s[l]] -= 1
            l += 1

    return result


if __name__ == "__main__":
    s = 'ABAB'
    print(longest_repeating_character_replacement(s, 2))
    s = 'AABABBA'
    print(longest_repeating_character_replacement(s, 1))
    s = 'ACBCBFA'
    print(longest_repeating_character_replacement(s, 1))
    s = 'ABCDEFGHIJK'
    print(longest_repeating_character_replacement(s, 1))
    s = 'AABABBA'
    print(longest_repeating_character_replacement_optimized(s, 1))