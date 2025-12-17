import heapq

def solution(scoville, K):
# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
    # hq = []
    # for n in scoville:
    #     heapq.heappush(hq, n)
    heapq.heapify(scoville)

    answer = 0 # 음식을 섞은 횟수를 저장하는 변수
    while True:
        a = heapq.heappop(scoville) # 제일 작은 항목을 pop, 반환
        if a < K: # K스코빌보다 크면 탈출
            if scoville: # 남은 음식이 없으면 -1
                answer += 1
                b = heapq.heappop(scoville) # 두번째로 작은 항목 pop
                mix = a + b * 2 # 섞기
                heapq.heappush(scoville, mix) # 섞은 값을 hq에 넣음
            else:
                return -1
        else:
            return answer

print(solution([1, 2, 3, 9, 10, 12], 7))

# x = [4, 3, 1, 2, 5, 6]
# heapq.heapify(x)
# print(x) # [1, 2, 4, 3, 5, 6]