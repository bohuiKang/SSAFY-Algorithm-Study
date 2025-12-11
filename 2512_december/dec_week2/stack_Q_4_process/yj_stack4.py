# 1. 실행 대기 큐(Queue)에서 대기중인 프로세스 하나를 꺼냅니다.
# 2. 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣습니다.
# 3. 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행합니다.
#   3.1 한 번 실행한 프로세스는 다시 큐에 넣지 않고 그대로 종료됩니다.


from collections import deque

def solution(priorities, location):
    answer = 0
    Q = deque(enumerate(priorities))  # 튜플 쌍 리턴

    while True:
        cur_index, cur_priority = Q.popleft()  # 1.

        # 더 높은 우선순위 있는지 파악
        has_higher_priority = False
        for index, priority in Q:
            if cur_priority < priority:  # 2.
                has_higher_priority = True
                break

        # 2. 더 높은 우선순위 있으면 다시 큐에 넣기
        if has_higher_priority:
            Q.append((cur_index, cur_priority))
        else:  # 3.
            answer += 1
            # 만약 원하는 프로세스가 빠져나갔으면 return answer
            if cur_index == location:
                return answer

print(solution([2, 1, 3, 2], 2))