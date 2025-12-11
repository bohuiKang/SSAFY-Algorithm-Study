def solution(progresses, speeds):
    answer = []
    days = []

    # 든 작업의 소요 일수를 구해서 days 리스트에 넣음
    for p, s in zip(progresses, speeds):
        # 남은 날짜 계산
        left_days = (100 - p + s - 1) // s
        # 각 progresses마다 필요한 날짜를 days라는 리스트에 저장
        days.append(left_days)

    max_day = days[0] # 첫 번째 작업이 걸리는 시간을 max_day로 기준 잡고 시작
    cnt = 0         # 이번 배포에 포함될 기능 개수

    for day in days:
        # 기준일 (max_day) 보다 빨리/동시에 끝나는 경우
        if day <= max_day:
            # 배포 가능 -> cnt += 1
            cnt += 1

        # 기준일보다 오래 걸리는 경우
        else:
            # 지금까지 누적된 count를 answer에 넣음
            answer.append(cnt)
            # cnt를 1로 초기화해줌
            cnt = 1
            # 기준일(max_day)을 현재 작업일(day)로 갱신
            max_day = day

    # 마지막에 남은 cnt 까먹지말고 answer에 추가해야돼염
    answer.append(cnt)

    return answer

#--------------------
# 큐 활용버전
from collections import deque

def solution(progresses, speeds):

    days = deque()
    for p, s in zip(progresses, speeds):
        days.append((100 - p + s - 1) // s)

    answer = []

    while days:
        # 첫 번째 기능이 배포되는 날짜를 기준으로 잡음
        standard = days.popleft()
        count = 1

        # 큐가 비어있지 않음 && 다음 기능이 기준일보다 빨리 끝난다면 계속 꺼냄
        while days and days[0] <= standard:
            days.popleft()
            count += 1

        answer.append(count)

    return answer