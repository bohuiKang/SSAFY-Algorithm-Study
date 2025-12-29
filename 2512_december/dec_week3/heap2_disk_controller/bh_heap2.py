import heapq

# 1. 작업의 소요시간이 짧은 것, 
# 2. 작업의 요청 시각이 빠른 것, 
# 3. 작업의 번호가 작은 것 순으로 우선순위가 높습니다.

def solution(jobs):
    n = len(jobs) # 몇개의 작업이 있는가?

    # 1. 작업의 번호(idx)를 포함하여 heapq에 저장
    hq_jobs = [] # heapq 에 저장하면, 정렬하지 않아도 작업 요청 시각 순으로 pop 된다.
    for idx, job in enumerate(jobs):
        heapq.heappush(hq_jobs, (job+[idx])) # [작업 요청 시각, 소요시간, 작업 번호]
    
    answer = 0 # 반환시간 저장 (작업 종료 시각 - 요청 시각)
    time = 0 # 현재 작업 시각
    cnt = 0 # 작업을 진행한 수
    hq_wait = [] # 작업 대기 큐

    # 2. 대기큐를 확인해서 작업 진행
    while n > cnt:

        # 2-1. time과 요청 시각을 비교해서 대기 큐에 작업 저장
        while hq_jobs: # 대기 큐에 넣을 작업이 있으면,
            s, l, idx = heapq.heappop(hq_jobs)
            if s <= time: # 작업 시각보다 작업 요청 시각이 작거나 같으면,
                heapq.heappush(hq_wait, ([l, s, idx])) # 대기큐에 저장
            else: # 크면 hq_jobs에 다시 넣고 while문 break
                heapq.heappush(hq_jobs, ([s, l, idx])) 
                break
        
        # 2-2. 작업 큐에 있는 작업 진행
        if hq_wait: # 대기큐에 작업이 있으면,
            long, start, work_n = heapq.heappop(hq_wait)
            time += long
            answer += time - start
            cnt += 1
        else: # 작업이 없으면,
            time += 1 # 현재 작업시각을 증가시켜, 대기 큐에 넣기

    # 3. 결과 리턴
    return answer // n

print(solution([[0, 3], [1, 9], [3, 5]]))