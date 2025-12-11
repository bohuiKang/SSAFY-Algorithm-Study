from collections import deque

def solution(priorities, location):
    q = deque()
    for i in range(len(priorities)):
        q.append([priorities[i], i])   # [우선순위, 인덱스]

    order = 0
    while q:
        temp = q.popleft()

        for node in q:
            if node[0] > temp[0]:      # 더 높은 우선순위 발견하면 뒤로 보냄
                q.append(temp)  
                break
        else:
            order += 1
            if temp[1] == location:
                return order
