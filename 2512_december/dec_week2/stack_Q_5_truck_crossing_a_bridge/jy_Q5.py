'''
트럭이 순서대로 들어감
'''

from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)

    current_weight = 0  # 다리 위에 있는 트럭들 무게 합
    time = 0

    while bridge:
        time += 1

        # 나가는 트럭 -> popleft로 다리에서 나간다
        bye_truck = bridge.popleft()
        current_weight -= bye_truck

        # 들어오는 트럭
        if trucks:
            # 다음 트럭이 올라와도 무게를 견딜 수 있는 경우
            if current_weight + trucks[0] <= weight:
                new_truck = trucks.popleft()
                # 이러면 다리 뒤에 트럭이 새로 들어옴
                bridge.append(new_truck)
                # 무게 추가해주기
                current_weight += new_truck

            # 다음 트럭이 올라올 시 무게를 초과하는 경우
            else:
                # 트럭 말고 0 추가
                bridge.append(0)

    return time