import heapq

def is_higher(scoville, K):
    """스코빌 지수가 모두 K 이상인지 확인"""
    for s in scoville:
        if s < K:  # 하나라도 K 미만이면 탈락
            return False
    else:
        return True        
    
def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)
    while True:
        if len(scoville) == 1:  # 음식이 한 개만 남을 때 까지 섞기
            break
        # 모두 스코빌 지수 K 이상인가?
        if is_higher(scoville, K) == True:
            return cnt
        # 모두 스코빌 지수 K 이상이 아니면 섞어야 함
        else:
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
            mixed = first + second * 2
            heapq.heappush(scoville, mixed)
            cnt += 1
            
    # 음식 하나만 남으면
    if is_higher(scoville, K) == True:
        return cnt
    else: return -1