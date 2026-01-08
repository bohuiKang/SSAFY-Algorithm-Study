# wire를 복사해서 한개씩 삭제하고 이걸로 리스트 구성해서 개수 비교 ㄱㄱ
def solution(n, wires):
    answer = -1
    min_val = float("inf")
    for i in range(n-1): # wires의 인자 하나씩 지워서 2개의 트리 만들어보기
        wires_copy = [wire[:] for wire in wires]
        wires_copy.pop(i)

        Tree = [[0]]+[[] for _ in range(n)]
        for v1, v2 in wires_copy: # 그래프 그리기 인덱스 번호가 해당 송전탑 번호 인접 리스트 표시
            Tree[v1].append(v2)
            Tree[v2].append(v1) 
        
        
        if not Tree[1]: # 1번에 연결된 송전탑 없을 경우 리스트가 비어있게 되므로 
            min_val = min(min_val, n-1)
            continue
        
        group_1 = [1]
        
        q = Tree[1][:] # 1번을 기준으로 개수를 세면 되니까 일단 q에 넣어줌
    
        while q:
            tower = q.pop()
            if tower not in group_1: # 연결된 group 만들어주기 그냥 set인 형태에서 add 해줘서 해도 될듯
                group_1.append(tower)

                for near_tower in Tree[tower]: # 해당 송전탑이랑 연결된 송전탑들의 연결된 송전탑들 q에 넣어주기 위해서
                    if near_tower not in group_1:
                        q.append(near_tower)
        
        val = abs(n-2*len(group_1))
        min_val = min(min_val, val)

    return min_val
            




print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]] ))
print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))