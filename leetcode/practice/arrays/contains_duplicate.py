def contains_duplicate(a):
    a_dict = {}
    for i in range(len(a)):
        if a[i] in a_dict:
            return True
        a_dict[a[i]] = i

    return False

def contains_duplicate_approach_2(a):
    return not(len(set(a)) == len(a))


if __name__ == "__main__":
    a = [1,2,3,4]
    print(contains_duplicate(a))
    print(contains_duplicate_approach_2(a))

