from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n # 컴퓨터 연결 확인 
    
    def is_connected(start):
        visited[start] = True # 시작 컴퓨터 True 처리
        q = deque([start])

        while q:
            node = q.popleft()
            for i in range(n):
                if not visited[i] and computers[node][i] == 1:
                    q.append(i) # 연결된 다음 컴퓨터 저장
                    visited[i] = True

        return 1 # 하나의 네트워크가 연결되었다. 
    
    for nxt in range(n):
        if not visited[nxt]:
            answer += is_connected(nxt) # 네트워크 저장.

    return answer 

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))