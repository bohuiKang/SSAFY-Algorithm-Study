def solution(str):
    stk = []
    for s in str:
        if s == '(':
            stk.append('(')
        else:
            # '('가 있을때만 pop, 아니면 return false
            if len(stk) > 0:
                stk.pop()
            else:
                return False
    if len(stk) == 0:
        return True
    else:
        return False