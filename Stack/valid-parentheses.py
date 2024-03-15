def validParentheses(s):
    stack = []
    for i in range(len(s)):
        if s[i] == '[' or s[i] == '{' or s[i] == '(':
            stack.append(s[i])
        else:
            pop = stack.pop()
            if pop == '{' and s[i] != '}':
                return False
            if pop == '[' and s[i] != ']':
                return False
            if pop == '(' and s[i] != ')':
                return False
    return True

print(validParentheses("()[]{}"))
print(validParentheses("()"))
print(validParentheses("[)"))