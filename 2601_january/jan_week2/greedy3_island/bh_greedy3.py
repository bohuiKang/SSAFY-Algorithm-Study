import heapq
# 최소 비용으로 섬 연결하기

def solution(n, costs):
    answer = 0

    # 인접 배열/리스트 생성
    adj_arr = [[0] * n for _ in range(n)]
    adj_list = [[] for _ in range(n)]

    for s, e, cost in costs:
        adj_arr[s][e] = cost    # 배열
        adj_arr[e][s] = cost

        adj_list[s].append(e)   # 리스트
        adj_list[e].append(s)

    ''' print(adj_arr)
    [  0  1  2  3
    0 [0, 1, 2, 0], 
    1 [1, 0, 5, 1], 
    2 [2, 5, 0, 8], 
    3 [0, 1, 8, 0]
    ]
    '''
    ''' print(adj_list)
    [
    0 [1, 2], 
    1 [0, 2, 3], 
    2 [0, 1, 3], 
    3 [1, 2]
    ]
    '''

    # 각 다리별로 다리 건설 시작
    for i in range(n):
        visited = [False] * n   # 모든 섬 연결 확인
        visited[i] = True   # 출발 섬은 True

        h = []

        start = i
        end_list = adj_list[start]
        for end in end_list:
            cost = adj_arr[start][end]
            # heapq 값 넣기
            heapq.heappush(h, (cost, end))   # 비용, 다음 섬
        
        total_cost = 0

        while h:
            cost, next = heapq.heappop(h)

            if not visited[next]:   # 연결이 안된 섬일 때
                visited[next] = True
                start = next
                total_cost += cost
                end_list = adj_list[start]

                for end in end_list:
                    if not visited[end]:    # 방문 안했을 때
                        cost = adj_arr[start][end]
                        # heapq 값 넣기
                        heapq.heappush(h, (cost, end))

        answer = min(answer, total_cost)

    return answer

# def build_bridge(n):

solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])



'''2번'''
'''import heapq
# 최소 비용으로 섬 연결하기

def solution(n, costs):
    answer = 0

    h = []
    visited = [False] * n   # 모든 섬 연결 확인

    for s, e, cost in costs: # 시작 섬, 다음 섬, 비용
        heapq.heappush(h, (cost, s, e))   # 비용, 시작 섬, 다음 섬

    cost, start, next = heapq.heappop(h)
    
    while h:
        cost, start, next = heapq.heappop(h)
        visited[start] = True

        if not visited[next]:   # 연결이 안된 섬일 때
            visited[next] = True
            start = next

    return answer

solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])'''