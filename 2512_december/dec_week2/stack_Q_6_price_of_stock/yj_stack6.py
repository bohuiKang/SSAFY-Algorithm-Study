from collections import deque

def solution(prices):
    Q = deque(prices)
    answer = []

    while Q:
        curPrice = Q.popleft()
        tmp = 0
        for q in Q:
            tmp += 1
            if curPrice > q:
                break
        answer.append(tmp)
    return answer

print(solution([1, 2, 3, 2, 3]))
# [4, 3, 1, 1, 0]