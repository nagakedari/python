def get_score_of_paranthesis(string):
    stack = []
    score=0
    for i in string:
        if i == '(':
            stack.append(i)
        else:
            if stack[-1] == '(':
                stack.pop()
                stack.append(1)
            else:
                count = 0
                while stack[-1] != '(':
                    count+= stack[-1]
                    stack.pop()
                stack.pop()
                stack.append(2 * count)
    while len(stack):
        score+= stack[-1]
        stack.pop()
    return score

# print(get_score_of_paranthesis('(()(()))'))


def scoreOfParentheses(S):
    def F(i, j):
        #Score of balanced string S[i:j]
        ans = bal = 0

        #Split string into primitives
        for k in range(i, j):
            bal += 1 if S[k] == '(' else -1
            print (i, j)
            if bal == 0:
                if k - i == 1:
                    ans += 1
                else:
                    ans += 2 * F(i+1, k)
                i = k+1

        return ans

    return F(0, len(S))

# print(scoreOfParentheses('(()(()))'))

def testF(S):
    def F(i, j):
        #Score of balanced string S[i:j]
        ans = bal = 0

        #Split string into primitives
        for k in range(i, j):
            bal += 1 if S[k] == '(' else -1
            print (i, j)
            print(bal)
            if bal == 0:
                if k - i == 1:
                    ans += 1
                else:
                    ans += 2 * F(i+1, k)
                i = k+1

        return ans

    return F(0, len(S))

print(testF('(()(()))'))