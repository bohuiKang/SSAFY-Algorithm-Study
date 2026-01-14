# 출발은 ICN -> 출발지가 ICN인 티켓들을 첫번째 depth의 후보로 넣음
# 티켓들의 연결 가능한 쌍을 단방향 간선할당
# 현재 티켓의 도착지를 기준 노드로 모든 티켓들의 출발지를 순회하여 같은 도시면 단방향 간선
 
# 티켓을 하나씩 사용하며 다음 depth로 넘어가는 재귀함수 구현
# 기저조건 : 모든 티켓을 사용했을 경우 answer에 해당 경로를 add (알파벳 순번이 빠른경우만)

    
def solution(tickets):
    graph = {}
    for u, ticket1 in enumerate(tickets):
        for v, ticket2 in enumerate(tickets):
            if ticket1[1] == ticket2[0]:
                graph.setdefault(u, []).append(v)

    start = [i for i, (a, b) in enumerate(tickets) if a == "ICN"]

    answer = []
    used = [False] * len(tickets)

    def recur(node, path, depth):
        nonlocal answer

        if depth == len(tickets):
            if not answer or path < answer:
                answer = path[:]
                return

        if node not in graph:
            return

        for nxt in graph[node]:
            if not used[nxt]:
                used[nxt] = True
                path.append(tickets[nxt][1])
                recur(nxt, path, depth + 1)
                path.pop()
                used[nxt] = False

    for s in start:
        used[s] = True
        recur(s, ["ICN", tickets[s][1]], 1)
        used[s] = False

    return answer
