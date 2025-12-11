from collections import deque

prices = [1, 2, 3, 2, 3]
def solution(prices):
    N = len(prices)
    answer = [0] * N
    q = deque(prices)
    i = 0
    while q and i < N-1:
        price = q.popleft()
        j = 0
        for next_p in q:
            if next_p < price: # 가격 하락시 break 가격 하락하는 순간도 시간에 포함
                j += 1
                break
            j += 1
        answer[i] = j
        i += 1 

    return answer

print(solution(prices))