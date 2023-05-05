import collections

# sorting approach O(nlogn)
def get_k_most_frequent_sorted(a, k):
    if len(a) < k:
        return
    element_frequency_map = {}
    for i in range(0, len(a)):
        element_frequency_map[a[i]] = 1 + element_frequency_map.get(a[i],0)
    sorted_dict = dict(sorted(element_frequency_map.items(), key=lambda x: x[1], reverse=True))
    res = []
    count = 0
    for key, val in sorted_dict.items():
        if count < k:
            res.append(key)
            count += 1
        else:
            break

    return res

# index storing approach O(n)
def get_k_most_frequent(a, k):
    if len(a) == k:
        return a
    ele_freq_dict = collections.Counter(a)
    index_arra = [None] * (len(a) + 1)
    for key, v in ele_freq_dict.items():
        if not index_arra[v]:
            index_arra[v] = [key]
        else:
            index_arra[v].append(key)
    res = []
    for i in range(len(index_arra)-1, 0, -1):
        if k <= 0:
            break
        if index_arra[i]:
            res.extend(index_arra[i])
            k -= 1
    return res




if __name__ == "__main__":
    a = [1,1,1,2,2,3]
    print(get_k_most_frequent_sorted(a, 2))
    print(get_k_most_frequent(a, 2))
    a = [1]
    print(get_k_most_frequent_sorted(a, 1))
    print(get_k_most_frequent(a, 1))


