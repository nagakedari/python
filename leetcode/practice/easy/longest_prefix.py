def longest_prefix(s):
    res = ""
    for tup in zip(*s):
        if len(set(tup)) == 1:
            res += tup[0]
        else:
            break
    return res


if __name__ == "__main__":
    s = ["flower","flow","flight"]
    print(longest_prefix(s))
    s = ["dog","racecar","car"]
    print(longest_prefix(s))