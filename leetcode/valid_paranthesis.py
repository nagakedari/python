def is_valid_paranthesis(string):
    open_paranthesis = ['{','(', '[']
    paranthesis_map = {
        ')' :'(',
        ']' : '[',
        '}' : '{'
    }
    stack = []
    for i in string:
        if i in open_paranthesis:
            stack.append(i)
        else:
            if stack[-1]== paranthesis_map[i]:
                stack.pop()
            else:
                return False
    return True

print('is string has valid paranthesis: {}'.format(is_valid_paranthesis('{[]}')))