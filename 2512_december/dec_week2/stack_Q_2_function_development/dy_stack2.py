import math
def solution(progresses, speeds):
    answer = []
    n = len(progresses)
    for i in range(n):
        # 100%완성까지 걸리는 기간으로 progresses 갱신
        # ceil, 올림 함수
        # (100 - 현재진도) / 속도 = 남은 일수 (올림 처리)
        progresses[i] = math.ceil((100 - progresses[i]) / speeds[i])
        
    # 현재 그룹의 첫 번째 기능 완료 일수
    prev = progresses[0]
    # 현재 그룹에 포함된 기능 개수
    cnt = 1
    for j in range(1, n):
        # 현재 기능이 이전 기능보다 먼저 또는 같은 날 완료되면
        # 같은 날 배포 가능 (앞 기능이 완료될 때까지 기다림)
        if prev >= progresses[j]:  
            cnt += 1
        else:
            # 아니라면 현재 기능 배포
            answer.append(cnt)
            # 직전값 갱신, 초기화
            prev = progresses[j]
            cnt = 1
    # 마지막 그룹 추가
    answer.append(cnt)  
    return answer