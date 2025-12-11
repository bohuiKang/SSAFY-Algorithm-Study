from collections import deque
priorities = [1, 1, 9, 1, 1, 1]	
location = 0

def solution(priorities, location):
    answer = 0
    size = len(priorities)
    max_val = max(priorities)
    i = 0
    while priorities[location]: # 해당 location 값이 0 되면 while 끝남
        if priorities[i] == max_val: # 최대값이랑 같으면 해당 인덱스 값을 0으로 바꿈
            priorities[i] = 0
            answer += 1
            max_val = max(priorities) # 최대값 갱신

        i = (i+1) % size  


            
    return answer


print(solution(priorities, location))