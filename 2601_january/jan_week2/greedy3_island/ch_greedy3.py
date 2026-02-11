from heapq import heappush, heappop

def solution(n, costs):
    graph = [[None] * n for _ in range(n)]
    for start, end, weight in costs:
        graph[start][end] = weight
        graph[end][start] = weight
    
    MST = [0] * n   # visited 역할
    pq = [(0, 0)]   # (가중치, 노드)
    min_weight = 0  # 최소 비용
    
    while pq:
        weight, node = heappop(pq)
        if MST[node]:
            continue
        MST[node] = 1
        min_weight += weight
        
        for next_node in range(n):
            weight = graph[node][next_node]
            
            if MST[next_node]:
                continue
            if weight == None:
                continue
            heappush(pq, (weight, next_node))
            
    return min_weight
        
        
