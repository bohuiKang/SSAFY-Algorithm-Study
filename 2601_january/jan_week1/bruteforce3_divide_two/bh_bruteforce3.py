from collections import deque

def solution(n, wires):
    answer = -1
    graph = {i: set() for i in range(n+1)} # 인접 리스트(set)
    gap = [] # 송전탑 개수 차이 저장 리스트

    # 특정 간선이 제거된 송전탑의 개수 차 확인 함수
    def check_pylon(): 
        visited = [False] * (n+1)

        q = deque()
        q.append(1)
        visited[1] = True
        cnt = 1
        while q:
            node = q.popleft()
            for end in graph[node]:
                if not visited[end]: # 송전탑 중복 체크
                    visited[end] = True
                    cnt += 1
                    q.append(end)
        return cnt

    for u, v in wires: # 인접 그래프 생성
        graph[u].add(v)
        graph[v].add(u)

    for u, v in wires: # 특정 간선 제거 / 복구
        graph[u].discard(v)
        graph[v].discard(u)

        cnt = check_pylon() # 연결된 송전탑 개수 차 구하기
        gap.append(abs((n-cnt)-cnt))

        graph[u].add(v)
        graph[v].add(u)

    answer = min(gap)
    return answer

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))