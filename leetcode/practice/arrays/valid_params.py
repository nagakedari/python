
def is_valid(s):
    stack = []
    parenthesis_map = {
        "}": "{",
        ")" : "(",
        "]" : "["
    }
    top = -1
    for i in range(0, len(s)):
        if len(stack) > 0 and s[i] in parenthesis_map and stack[top] == parenthesis_map[s[i]]:
            stack.pop(top)
            top -= 1
        else:
            stack.append(s[i])
            top += 1

    return len(stack) == 0


if __name__ == "__main__":
    # s = "()([[{}]]){{{{}]})"
    s = "(((({{{{[[[[]]]]}}}}))))"
    print(is_valid(s))

