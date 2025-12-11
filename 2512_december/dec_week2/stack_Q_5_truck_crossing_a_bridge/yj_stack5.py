from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    idle = deque(truck_weights)  # 대기 트럭
    go = deque([])  # 다리를 건너는 트럭

    while idle or go:  # 대기중이거나 다리 건너는 트럭 있으면 continue
        answer += 1  # 1초 경과

        # 건너는 중인 트럭 이동길이 +1
        if go:
            for truck in go:
                truck[1] -= 1

            # 다리 다 건넌 트럭 제거
            while go and go[0][1] == 0:  # 한 번에 여러 트럭 동시에 들어갔다 나오는 경우
                go.popleft()

        # 새로 들어갈 트럭
        if idle:
            cur_weight = sum(truck[0] for truck in go)  # 들어갈 수 있는지 길 위의 트럭 무게 합 확인
            gonna_start = idle[0]  # 출발하려는 차

            if cur_weight + gonna_start <= weight:
                go.append([idle.popleft(), bridge_length])  # [트럭 무게, 건너야하는 길이]

    return answer

print(solution(2, 10, [7, 4, 5, 6]))
# 8