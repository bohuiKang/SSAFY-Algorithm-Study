def solution(number, k):
    stack = []
    cnt = k

    for n in number:
        # 스택이 있고, 스택 끝번호가 n 보다 작고, cnt 값이 남아 있을 때,
        while stack and stack[-1] < n and cnt > 0:
                stack.pop()
                cnt -= 1
        stack.append(n)
    
    if cnt:
         stack = stack[:-cnt] # 뒤에서 부터 cnt 까지 제거

    return ''.join(stack)

print(solution("1231234", 3))
# "1231234"	3	"3234"
# number="54321", k=2