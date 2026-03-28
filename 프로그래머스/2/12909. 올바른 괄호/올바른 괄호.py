def solution(s):
    if s[0] == ')' or s[-1] == '(':
        return False
    
    stack = []
    for str in s:
        if str == '(':
            stack.append(str)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False