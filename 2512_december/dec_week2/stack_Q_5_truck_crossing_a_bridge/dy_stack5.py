from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 시간 변수
    t = 0
    
    # 다리 큐로 생성
    bridge = deque([0] * bridge_length)
    
    # 현재 다리 위 총 무게
    current_weight = 0
    
    # 트럭 무게로 이뤄진 트럭 목록, 큐로 생성
    trucks = deque(truck_weights)
    
    # 대기 중인 트럭이 있는 동안 반복
    while trucks:
        # 1초 경과
        t += 1
        
        # 다리 맨 앞에서 하나 빼기 (트럭이 다리를 완전히 건너거나 빈 공간)
        exited = bridge.popleft()
        current_weight -= exited  # 빠진 트럭 무게만큼 감소
        
        # 다음 트럭을 올릴 수 있는지 체크
        if current_weight + trucks[0] <= weight:
            # 무게 제한 OK → 트럭을 다리에 올림
            truck = trucks.popleft()
            bridge.append(truck)
            current_weight += truck
        else:
            # 무게 제한 초과 → 빈 공간(0)만 넣어서 시간만 흐르게 함
            # 다리 위 트럭이 앞으로 이동하는 시간 벌기
            bridge.append(0)
    
    # 마지막 트럭이 다리를 완전히 건너는 시간 추가
    # trucks가 비었어도 다리 위에는 아직 트럭이 있음
    t += bridge_length
    
    return t