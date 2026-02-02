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
# 그런데 
def solution(n, costs):
    answer = 0
    check_num = [0]*n
    # cost 기준으로 정렬
    costs.sort(key= lambda x: x[2])
    
    for i, j, cost in costs:
        pass
    
        
        
    return answer


print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]	))
