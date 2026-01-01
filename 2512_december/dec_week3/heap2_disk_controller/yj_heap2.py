import heapq

def solution(jobs):
    # 1. 요청 시간 빠른 순대로 정렬
    jobs.sort()
    
    answer = 0  # 총 대기/처리 시간의 합
    now = 0  # 현재 시각
    i = 0  # jobs 리스트의 인덱스 ( 몇 번째 작업까지 확인했는지)
    count = 0  # 완료된 작업 개수
    wait_list = []  # 현재 실행 대기중인 작업들
    
    # 모든 작업을 완료할 때 까지 반복
    while count < len(jobs):
        # 1. 현재 시각까지 도착한 모든 작업 힙에 넣기
        # jobs[i][0]은 요청 시점
        while i < len(jobs) and jobs[i][0] <= now:
            # 힙에는 (소요시간, 요청시점)
            heapq.heappush(wait_list, [jobs[i][1], jobs[i][0]])
            i += 1
            
        # 2. 처리할 작업 있는지 확인
        if wait_list:
            # 대기 중인 작업 중 가장 소요시간 짧은것 꺼내기
            duration, request_time = heapq.heappop(wait_list)
            
            # 작업 처리
            # 현재 시각 업데이트
            now += duration
            # 이번 작업의 (대기시간 + 처리시간) 계산해서 합치기
            # (끝난 시각 - 요청 시각)이 실제 걸린 총 시간임
            answer += (now - request_time)
            # 완료 작업 개수 증가
            count += 1
        else:
            # 지금 처리할 작업이 없다면
            # 다음 작업 시간으로 점프
            now = jobs[i][0]
            
    # 평균 시간을 구해야 하므로 전체 작업 개수로 나눔
    return answer // len(jobs)
