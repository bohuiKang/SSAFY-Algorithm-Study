from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)
    total = 0           # 다리 위 현재 총 무게
    trucks = deque(truck_weights)

    while bridge:
        time += 1
        total -= bridge.popleft()       # 다리 맨 앞 트럭 건넘

        if trucks:
            if total + trucks[0] <= weight:
                temp = trucks.popleft()   # 다음 트럭 진입
                bridge.append(temp)
                total += temp
            else:
                bridge.append(0)       # 무게초과면 한턴 쉼

    return time
