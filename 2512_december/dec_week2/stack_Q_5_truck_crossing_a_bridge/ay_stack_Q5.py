from collections import deque
bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque()
    total_weight = 0
    trucks = deque(truck_weights)
    bridge_num = 0

    while trucks or bridge:
        time += 1

        if bridge and bridge[0][1] == time:
            w, _ = bridge.popleft()
            total_weight -= w
            bridge_num -= 1

        if trucks and total_weight + trucks[0] <= weight and bridge_num < bridge_length: # 들어갈 트럭 무게 더했을떄 넘치지 않으면 + 다리 길이보다 다리위 트럭수 적으면
            w = trucks.popleft()
            total_weight += w
            bridge.append((w, time+bridge_length))
            
    return time

print(solution(bridge_length, weight, truck_weights))
        

# def solution(bridge_length, weight, truck_weights):
#     answer = 0
#     sum_weight = 0
#     in_bridge = []
#     for truck in truck_weights:
#         sum_weight += truck
        
#     q = deque(truck_weights[::-1])
    
#     total_time = 0
#     while q:
#         truck = q.pop()
#         cnt = 1
#         time = bridge_length
#         sum_weight = truck

#         while q:
#             next_truck = q.pop()
#             if sum_weight + next_truck > weight:
#                 q.append(next_truck)
#                 break
#             sum_weight += next_truck
#             cnt += 1
#             time += 1
            
#         if not q:
#             time += 1

#         total_time += time



#     return total_time

# print(solution(bridge_length, weight, truck_weights))