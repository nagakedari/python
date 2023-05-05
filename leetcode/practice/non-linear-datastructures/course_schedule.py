def can_complete_all_course(pre_req, no_of_course):
    course_preq_map = {i: [] for i in range(no_of_course)}
    for c, pre in pre_req:
        course_preq_map[c].append(pre)

    visited = set()

    def dfs(curr_c):
        if curr_c in visited:
            return False
        if course_preq_map[curr_c] == []:
            return True
        visited.add(curr_c)
        for pre in course_preq_map[curr_c]:
            if not dfs(pre):
                return False
        visited.remove(curr_c)
        course_preq_map[curr_c] = []
        return True

    for c in range(no_of_course):
        if not dfs(c):
            return False
    return True



if __name__ == "__main__":
    pre_req = [[1, 0]]
    print(can_complete_all_course(pre_req, 2))

    pre_req = [[1, 0], [0, 1]]
    print(can_complete_all_course(pre_req, 2))

    pre_req = [[1, 0], [3, 2], [0, 3]]
    print(can_complete_all_course(pre_req, 4))

    pre_req = [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]
    print(can_complete_all_course(pre_req, 5))