def find_user_id_with_error(action_error_pairs, action_sequence):
    user_action_hash = {}
    user_ids = []
    for action_error_pair in action_error_pairs:
        userid = action_error_pair[1]
        action = action_error_pair[0]
        if userid in user_action_hash.keys():
            user_action_hash[userid]+= action
        else:
            user_action_hash[userid] = action
    for key in user_action_hash.keys():
        if action_sequence in user_action_hash[key]:
            user_ids.append(key)
    return user_ids

action_user_1 = [
["A", "1"],
["B", "1"],
["B", "2"],
["C", "1"],
["C", "2"],
["C", "3"],
["A", "2"],
["A", "3"],
["A", "2"],
["B", "2"],
["C", "2"],
]
print(find_user_id_with_error(action_user_1, "ABC"))
action_user_2 = [
["A", "1"],
["A", "1"],
["A", "1"],
["B", "1"],
["B", "2"],
["C", "2"],
["C", "2"],
["C", "3"],
["A", "2"],
["A", "3"],
["A", "2"],
["B", "2"],
["C", "2"],
]

print(find_user_id_with_error(action_user_2, "ABC"))