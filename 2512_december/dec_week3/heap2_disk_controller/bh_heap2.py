import heapq

# 1. 작업의 소요시간이 짧은 것, 
# 2. 작업의 요청 시각이 빠른 것, 
# 3. 작업의 번호가 작은 것 순으로 우선순위가 높습니다.
def solution(jobs):
    answer = 0
    time = 0
    hq = []
    for job in jobs:
        s, l = job # start, long(소요 시간)
        heapq.heappush(hq, (l, s)) 
        
        for _ in range(l):
            time += 1
            if 
    while True:
        
    return answer

