def parent_child_count(parent_child_pair_list):
    child_occurance_hash = {}
    parents_set = set()
    for parent_child_pair in parent_child_pair_list:
        parents_set.add(parent_child_pair[0])
        child = parent_child_pair[1]
        if child in child_occurance_hash.keys() :
            child_occurance_hash[child]+=1
        else:
            child_occurance_hash[child] = 1
    keys = child_occurance_hash.keys()
    childs_with_1_parent = [key for key in keys if child_occurance_hash[key]==1]
    childs_with_0_parent = [child for child in parents_set if child not in keys]
    return childs_with_0_parent, childs_with_1_parent

print(parent_child_count([
(1, 3), (2, 3), (3, 6), (5, 6), (15, 9),
(5, 7), (4, 5), (4, 8), (4, 9), (9, 11)
]))