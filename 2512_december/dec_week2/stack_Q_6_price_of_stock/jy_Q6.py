def solution(prices):

    n = len(prices)
    answer = [0] * n

    for i in range(n):
        for j in range(i + 1, n):
            answer[i] += 1

            # 가격이 상승되었어요 ...
            if prices[i] > prices[j]:
                break

    return answer

p = list(map(int, input().split()))
print(solution(p))