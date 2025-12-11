def solution(s):
    stack = []
    for p in s:
        if p == '(':
            stack.append(p)
        elif p == ')':
            if not stack: # 괄호가 비어있다면
                return False
            stack.pop()
            
    if stack: # 괄호가 남아있다면
        return False

    return True