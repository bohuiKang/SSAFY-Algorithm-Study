import heapq
def solution(scoville, K):
    # 힙큐로 변환
    heapq.heapify(scoville)
    # 섞은 횟수
    answer = 0
    # 힙큐에서 가장 맵지 않은 게 K이상이 될때까지 반복
    while scoville[0] < K:
        # 힙큐안의 요소가 2개 이상이 되지 않는다면 섞을 수 없으니 -1로 갱신 후, 반복문을 종료
        if len(scoville) < 2:
            answer = -1
            return answer
        # 가장 맵지 않은, 2번째로 맵지않은 것을 꺼낸 후 섞고 횟수 갱신
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        mixed = first + second*2
        heapq.heappush(scoville, mixed)
        answer += 1
    return answer