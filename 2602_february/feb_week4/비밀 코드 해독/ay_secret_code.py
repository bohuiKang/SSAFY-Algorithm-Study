from itertools import combinations

def solution(n, q, ans):
    m = len(q)
    q_sets = [set(row) for row in q]
    
    ban = set()
    # ans =5, 0 먼저 확인
    for i, a in enumerate(ans):
        if a == 5:
            return 1
        # ans = 0 이면 조합에서 빼야함
        elif a == 0:
            ban |= q_sets[i]
    
    # ban에 들어간 숫자
    nums = [x for x in range(1, n + 1) if x not in ban]

    answer = 0
    # 조합 생성하고
    for comb in combinations(nums, 5):
        comb_set = set(comb)
        # 교집합 구했을 때 길이가 ans[i] 랑 맞으면 
        for i in range(m):
            if len(comb_set & q_sets[i]) != ans[i]:
            
                break
        else:
            answer += 1


    return answer