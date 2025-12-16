import heapq
# 최솟값을 빼내고 다시 값을 리스트에 넣어야 하기 때문에 heap을 쓰는것이 시간을 덜 쓴다.

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while len(scoville) > 1: # heapq에 1개 남을 떄 까지 -> 1개 남고 K 이상이 안되면 second 값이 없어서 에러 날 것으로 보여 1개에서 끊음
        first = heapq.heappop(scoville)

        if first >= K: # 제일 작은 값이 K이상
            return answer

        second = heapq.heappop(scoville)
        mix = first + (second * 2)
        answer += 1
        heapq.heappush(scoville, mix)

    if heapq.heappop(scoville) < K: # 조건 만족 못하는 경우
        return -1

    return answer

print(solution([1, 2, 3, 9, 12, 10], 7))