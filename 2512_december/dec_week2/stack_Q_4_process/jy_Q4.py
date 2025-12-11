def solution(priorities, location):
    # 중요도가 높은 순서대로 정렬시킴
    sorted_priorities = sorted(priorities, reverse=True)

    answer = 0

    while True:
        for i, priority in enumerate(priorities):
            # 현재 인덱스의 중요도 == 지금 남은 것 중 가장 높은 중요도(sorted_priorities[answer])랑 같다면
            if priority == sorted_priorities[answer]:
                # answer을 1 증가시킴 -> 다음 중요도로 이동
                answer += 1

                # 현재 위치(i) == 내 프로세스(location)라면 정답 !!!
                if i == location:
                    return answer