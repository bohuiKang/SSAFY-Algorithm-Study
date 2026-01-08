def solution(n, wires):
    # 트리라고는 하는데 양방향 간선이라 그래프로

    # 1. 양방향 간선할당
    graph = {}
    for u, v in wires:
        graph.setdefault(u, []).append(v)
        graph.setdefault(v, []).append(u)

    # 2. 끊어진 간선을 고려한 DFS 구현 (start 지점은 아무곳에서나 상관없음)
    def DFS(start, divide):
        stack = [start]
        visited = set()
        cnt = 0
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                cnt += 1
                for next_node in graph[node]:
                    if node in divide and next_node in divide:  # 잘린 간선이면 건너뜀
                        continue 
                    stack.append(next_node)
        return cnt

    # 3. 모든 간선들을 하나씩 끊어보면서 DFS 완탐
    min_v = float('inf')
    for node, next_node in wires:
        divide = (node, next_node)
        cnt = DFS(node, divide)
        diff = abs((n - cnt) - cnt) # 두 전력망의 송전탑 개수차의 절대값
        min_v = min(min_v, diff)
    answer = min_v
    return answer
