def is_anagram(s, t):
    if len(s) != len(t):
        return False
    s_dict = {}
    t_dict = {}
    for i in range(0, len(s)):
        if s[i] in s_dict:
            s_dict[s[i]] += 1
        else:
            s_dict[s[i]] = 1
        if t[i] in t_dict:
            t_dict[t[i]] += 1
        else:
            t_dict[t[i]] = 1

    return s_dict == t_dict


if __name__ == "__main__":
    print(is_anagram("rat", "car"))

