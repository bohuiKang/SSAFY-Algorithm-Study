from collections import deque

def solution(s):
    stack = deque()
    answer = False
    
    # 순회하며 괄호 검사
    for char in s:
        if char == '(':
            # 여는 괄호는 스택에 push
            stack.append(char)
        else:  # char == ')'
            # 닫는 괄호가 나왔는데 스택이 비어있으면 False
            if not stack:
                return answer
            # 스택에 여는 괄호가 있으면 pop (짝 맞추기)
            stack.pop()
    
    # 스택이 비어있으면 모든 괄호가 짝을 이룬 것
    if len(stack) == 0:
        answer = True
        
    return answer