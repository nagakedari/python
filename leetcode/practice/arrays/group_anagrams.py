
def is_valid_anagram(s, t):
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


def group_anagrams(a):
    ans = []
    stack = a.copy()
    peek = len(stack)-1
    while peek >= 0:
        s = stack[peek]
        anagrams = [s]
        for i in range(0, len(a)):
            t = a[i]
            if s != t and is_valid_anagram(s, t):
                anagrams.append(t)
                stack.pop(i)
                peek -= 1
        peek -=1
        ans.append(anagrams)
    print(ans)


def group_anagrams_sorting_approach(a):
    ans = []
    anagram_dict = {}
    for i in range(0, len(a)):
        sorted_i = str("".join(sorted(a[i])))
        # print(f"sorted_i: {sorted_i}")
        # print(f"dict: {anagram_dict}")
        if sorted_i in anagram_dict:
            anagram_dict[sorted_i].append(a[i])
        else:
            anagram_dict[sorted_i] = [a[i]]

    print([items for k, items in anagram_dict.items()])


if __name__ == "__main__":
    a = ["eat", "tea", "tan", "ate", "nat", "bat"]
    group_anagrams_sorting_approach(a)
    # group_anagrams(a)
    a = [""]
    group_anagrams_sorting_approach(a)
    a = ["a"]
    group_anagrams_sorting_approach(a)

