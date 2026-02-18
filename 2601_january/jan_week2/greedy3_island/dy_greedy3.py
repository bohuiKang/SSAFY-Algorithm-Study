# mst 문제라고 가정
# prim 아님 kruskal 
# kruskal은 간선 기준(간선 비용이 작은 순대로 정렬 후 부모가 같지 않다면 union 후 비용 추가
# prim은 노드 기준(한 노드에서 비용이 가장 적은 간선의 노드로 확장, 방문처리로 사이클 방지?, 얘는 시작 노드가 어디든 상관 없나? )

from collections import defaultdict
from heapq import heappop, heappush

'''
def solution(n, costs):
    answer = 0
    heap = []
    lst = defaultdict(list)
    for x,y,c in costs:
        heappush(heap, (c, x, y))
        lst[x].append((y))
        lst[y].append((x))
'''

def solution(n, costs):

    def find_set(x):
        while x != parents[x]:
            x = parents[x]
        return x

    costs.sort(key=lambda x:x[2])
    parents = [a for a in range(n)]
    distance, cnt = 0, 0

    for x, y, dis in costs:
        if find_set(x) != find_set(y):
            parents[find_set(y)] = find_set(x)
            distance += dis
            cnt += 1

            if cnt >= n-1:
                break

    return distance

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))