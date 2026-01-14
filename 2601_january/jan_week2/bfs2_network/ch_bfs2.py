# 컴퓨터들이 대칭적으로 연결되므로 그래프 구현시에 유향으로 해도 상관없음
# 컴퓨터의 번호는 2차원 리스트 arr의 인덱스

# for문으로 arr을 돌려서 i = j 일때는 건너뛰고 나머지 경우에서 arr[i][j] == 1이면
# i번 정점에서 인접정점 j번으로 유향간선 할당

# arr의 길이가 컴퓨터의 개수 -> for문으로 함수를 호출해서 함수가 작동되면 cnt += 1
# 함수는 dfs로 연결된 컴퓨터 만큼 탐색하여 visited에 넣는 구조 (visited를 전역변수로 공유해야함)

# n: 컴퓨터의 개수, computers: 2차원배열

# DFS 함수 구현
def DFS(com):
    global visited
    stack = [com]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(graph[node])

# 그래프 구현 (간선할당)
graph = {}
def get_graph(n, computers):
    global graph
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:  # 서로 연결된 컴퓨터면 간선할당
                graph.setdefault(i, []).append(j)

visited = set()
# 반환함수
def solution(n, computers):
    global visited
    get_graph(n, computers)
    cnt = 0
    for com in range(n):    # 컴퓨터의 번호마다 연결된 네트워크 있는지 확인
        if com not in visited:
            DFS(com)
            cnt += 1
    return cnt