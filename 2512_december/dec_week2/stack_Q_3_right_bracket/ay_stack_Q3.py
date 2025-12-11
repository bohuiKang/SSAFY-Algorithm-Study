s = "(()("

def solution(s):
    answer = True
    stack = []
    for c in s:
        if c == "(":
            stack.append("(")
        else:
            if not stack:
                return False
            stack.pop()
    
    if stack:
        return False

    return True

print(solution(s))