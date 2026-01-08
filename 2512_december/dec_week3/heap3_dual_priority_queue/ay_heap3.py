# import heapq as hq

from collections import deque

def solution(operations):

    answer = deque([])
    for com in operations:
        command, num = com.split()
        if command == "I":
            answer.append(int(num))
            answer = deque(sorted(list(answer)))
        elif command == "D":
            if not answer:
                continue

            if num == "1":
                answer.pop()
            else:
                answer.popleft()
    
    if answer:
        return[answer[-1], answer[0]]
    else:
        return [0, 0]
    
print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))