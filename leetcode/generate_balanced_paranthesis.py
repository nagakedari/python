def generate_balanced_paranthesis(string, n):
    
    def _generate_balanced_paranthesis_helper(string, pos, n, open, close):
        if close == n:
            for i in string:
                print(i, end= "")
            print()
            return 
        else:
            if open < n :
                string[pos] = '{'
                _generate_balanced_paranthesis_helper(string, pos+1, n, open+1, close)
            if close < open:
                string[pos] = '}'
                _generate_balanced_paranthesis_helper(string, pos+1, n, open, close+1)
    if n > 0:
        _generate_balanced_paranthesis_helper(string, 0, n, 0, 0)
    return
n=3
string = [""] * 2 * n
generate_balanced_paranthesis(string, n)