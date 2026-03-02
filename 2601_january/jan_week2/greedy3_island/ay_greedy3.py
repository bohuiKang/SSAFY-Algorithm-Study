# 가장 작은 비용 부터?
# 
'''
    1 -(3) - 2
    |     /  |
    (3) (2) (1)
    |  /     |
    3- (4) - 4
선택을 2-4를 먼저하고 2-3 
1-
'''
# n개 체크 리스트 만들고 -> 인덱스로 체크
# costs -> costs 작은 순으로 정렬
# 아직 리스트 1로 안 바뀌었으면 포함하도록 진행
# 그런데 갑자기 생각났음!!
# 이렇게 되면 이어진것을 판별을 못함 이어지는 길을 탐색을 해야함
# 부모가 필요 - 오 생각한게 맞았네


def solution(n, costs):
    answer = 0
    parent = [0]*n
    # cost 기준으로 정렬
    costs.sort(key= lambda x: x[2])
    parents = [0]*n
    # 초기 부모 지정 - 자기자신
    for i in range(n):
        parents[i] = i
    
    # 부모 노드 넣어주기 -> 이거 lambda로 쓰면 줄여서 쓸 수 있을듯
    for i in range(n):
        parent[i] = i
    
    # find 
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])

        return parent[x]
    
    # union
    def union(a, b):
        a = find(a)
        b = find(b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
    
        
        
    return answer


print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]	))
