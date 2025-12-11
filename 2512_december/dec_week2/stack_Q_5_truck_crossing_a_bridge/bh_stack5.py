# 문제 이해가 안됨..

from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 다리에 올라갈 수 있는 트럭 수, 다리가 견디는 무게, 트럭의 무게 리스트
    stack = truck_weights[::-1] # 뒤집어서 저장
    answer = 1 # 소요시간
    driving = deque()
    driving_weight = 0 # 다리 위의 트럭 무게
    
    while stack:
        truck = stack.pop()
        # 운행트럭 수가 제한보다 적고, 운행트럭 무게 합이 다리 최대 하중보다 낮다면, 
        if len(driving) < bridge_length and driving_weight + truck <= weight: 
            driving_weight += truck
            driving.append((truck, 1)) # 트럭_무게, 시간
            answer += 1
        else: # 트럭수를 넘거나 다리 최대 하중을 넘는다면, 다음에 건너기 위해 append하기 
            stack.append(truck)
        for _ in range(len(driving)):
            truck_check, time = driving.popleft() # 다리 건넜는지 확인
            if time + 1 < 3:
                driving.append((truck_check, time + 1))
            else: # 트럭이 다리 다 건넘
                driving_weight -= truck_check
    return answer