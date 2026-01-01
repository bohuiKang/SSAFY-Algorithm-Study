# heapq는 튜플이나 리스트의 첫 번째 요소를 기준으로 우선순위를 결정하여 힙을 구성
import heapq

def solution(jobs):
    # 총 대기시간의 합
    answer = 0
    # 작업의 수
    n = len(jobs)
    # 현재 시간
    current_time = 0  
    
    # 요청 시간 기준으로 정렬
    jobs.sort()
    
    # 처리 대기 중인 작업들 (소요시간 기준 최소힙)
    heap = []
    # jobs의 인덱스
    idx = 0 
    # 완료된 작업 수
    completed = 0  
    
    # 모든 작업을 처리할 때까지 반복
    while completed < n:
        # 현재 시간까지 도착한 모든 작업을 힙에 추가
        while idx < n and jobs[idx][0] <= current_time:
            # (소요시간, 요청시간) 형태로 힙에 추가
            # 소요시간이 짧은 작업이 우선순위가 높음
            heapq.heappush(heap, (jobs[idx][1], jobs[idx][0]))
            idx += 1
        
        # 처리할 작업이 있으면 처리
        if heap:
            # 소요시간이 가장 짧은 작업 꺼내기
            duration, request_time = heapq.heappop(heap)
            # 현재 시간 갱신
            current_time += duration
            # 대기시간 = (작업 종료 시간) - (작업 요청 시간)
            answer += current_time - request_time
            completed += 1
        else:
            # 처리할 작업이 없으면 다음 작업이 올 때까지 시간 이동
            current_time = jobs[idx][0]
    
    # 평균 대기시간 반환 (소수점 버림)
    return answer // n