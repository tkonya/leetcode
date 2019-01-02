def checkValidString(s):
    print('og string: ' + s)
    s = remove_isolated_parens(s)
    print('sm string: ' + s)

    # quick checks for invalid
    if len(s) > 0 and (s[0] == ')' or s[len(s) - 1] == '('):
        return False  # starting close or ending open is invalid, no way to correct

    return recursive_check(s)


# will remove all instances of '()' from the
def remove_isolated_parens(s):

    if len(s) >= 2:
        if s[len(s) - 2] == '(' and s[len(s) - 1] == ')':
            return remove_isolated_parens(s[:len(s) - 2])
        for i in range(0, len(s) - 2):
            if s[i] == '(' and s[i + 1] == ')':
                return remove_isolated_parens(s[:i] + s[i + 2:])

    return s


def recursive_check(s):
    stack = ''

    if abs(s.count('(') - s.count(')')) > s.count('*'):
        return False  # cannot correct imbalance

    for i, c in enumerate(s):
        if len(stack) == 0 and c == ')':
            return False
        elif c == '*':
            if recursive_check(stack + '(' + s[i + 1:]):
                return True
            elif recursive_check(stack + s[i + 1:]):
                return True
            elif recursive_check(stack + ')' + s[i + 1:]):
                return True
            elif c == '(':
                stack += '('
            elif c == ')' and stack[len(stack) - 1] == '(':
                stack = stack[:len(stack) - 1]

    return len(stack) == 0


print(checkValidString("()*((()(((((*))))((*()((*(())()(**)()()*))((((()**((())((()()(()(()()*)()))(()))))))*(((()()()())()"))