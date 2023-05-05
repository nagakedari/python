# # My solution
# def two_sum(a, target):
#     a_dict = {v: k for k, v in enumerate(a)}
#     for i in range(0, len(a)):
#         diff = target - a[i]
#         if a_dict.get(diff):
#             return [i, a_dict[diff]]
#
#
# if __name__ == "__main__":
#     a = [2, 7, 11, 15]
#     print(two_sum(a, 18))


# Better Solution
def two_sum_better(a, target):
    a_dict = {}
    for i in range(0, len(a)):
        diff = target - a[i]
        if diff in a_dict:
            return [a_dict[diff], i]
        a_dict[a[i]] = i


if __name__ == "__main__":
    a = [2, 7, 11, 15]
    print(two_sum_better(a, 9))