def remove_outer_parantheses(string):
    stack= []
    for i in string:
        if len(stack) == 0:
            stack.append(i)
        elif i != stack[-1]:
            stack.append(i)
    print(''.join(stack))

remove_outer_parantheses('(()())(())(()(()))')