def solution(number, k):
    stack = []  # 숫자를 담을 바구니

    for num in number:
        # 스택에 뭐 있고
        # 스택의 마지막 요소가 지금 들어올 num보다 작고
        # 아직 지울 기회가 남음
        while stack and stack[-1] < num and k > 0:
            stack.pop()  # 작은 수 제거
            k -= 1  # 제거 횟수 -1

        stack.append(num)  # 스택에 num 추가

    # 숫자가 내림차순이라 아무것도 못 잘라내거나 남은 경우 -> 그냥 남은 k만큼 잘라 ,,,
    if k > 0:
        stack = stack[:-k]

    return "".join(stack)