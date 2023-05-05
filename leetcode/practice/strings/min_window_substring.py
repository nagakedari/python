
def min_window_substring(s, t):
    s_len, t_len = len(s), len(t)
    if t_len == "": return ""
    if s_len < t_len:
        return ""
    l, r, have_count = 0, 0, 0
    w_map = {}
    t_map = {}
    result, result_len = [], float("infinity")
    for i in range(0, t_len):
        if t[i] in t_map:
            t_map[t[i]] += 1
        else:
            t_map[t[i]] = 1
    while r < s_len:
        w_map[s[r]] = 1 + w_map.get(s[r], 0)
        if s[r] in t_map and w_map[s[r]] <= t_map[s[r]]:
            have_count += 1
        while have_count == t_len:
            if (r-l+1) < result_len:
                result = [l, r]
                result_len = r-l+1
            # pop from left of the window
            w_map[s[l]] -= 1
            if s[l] in t_map and w_map[s[l]] < t_map[s[l]]:
                have_count -= 1
            l += 1
        r += 1
    if result_len != float("infinity"):
        l, r = result
        return s[l: r+1]
    else: return ""




if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    print(min_window_substring(s, t))
    s = "a"
    t = "a"
    print(min_window_substring(s, t))
    s = "a"
    t = "aa"
    print(min_window_substring(s, t))
    s = "ABCBDOBECODEBANC"
    t = "ABC"
    print(min_window_substring(s, t))
    s = "AAAAADOBECODEBANCBBV"
    t = "AAABC"
    print(min_window_substring(s, t))
    s = "DCFGNBWRGH"
    t = "ABC"
    print(min_window_substring(s, t))
    s = "bbaa"
    t = "aba"
    print(min_window_substring(s, t))
