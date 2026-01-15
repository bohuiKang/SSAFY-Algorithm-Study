from collections import defaultdict

def solution(tickets): # 항상 "ICN" 공항에서 출발
    answer = [] 
    N = len(tickets)
    travel_dict = defaultdict(list) # 'ICN': ['ATL', 'SFO']
    for start, end in sorted(tickets, reverse=True): # 내림차순으로 입력되게 => pop() 사용
        travel_dict[start].append(end)

    print(travel_dict)

    stack = ["ICN"] # ICN 입력
    while stack:
        top = stack[-1] # 맨 뒤의 값을 호출

        if travel_dict[top]:
            stack.append(travel_dict[top].pop())
        else:
            answer.append(stack.pop())

    return answer[::-1] # 반전

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
print(solution([["ICN", "COO"], ["ICN", "BOO"], ["COO", "ICN"]]))