import math

def solution(progresses, speeds):
    works = len(progresses) # 작업 개수
    working_days = [0] * works # 100%가 되기위해 필요한 작업 일수
    work_done = [False] * works # 배포 완료 체크
    answer = [] # 정답 배열

    for i in range(works):
        spend_time = math.ceil((100 - progresses[i]) / speeds[i]) # 올림
        working_days[i] = spend_time
        
    for i in range(works):
        if not work_done[i]: # 아직 배포되지 않은 작업
            done_cnt = 0 # 한번에 배포 가능한 작업 수량 저장 변수
            for j in range(i, works):
                if working_days[i] >= working_days[j]:
                    done_cnt += 1
                    work_done[j] = True
                else: # 비교 작업 일수보다 값이 크면 for문 탈출
                    break
            answer.append(done_cnt)
            
    return answer