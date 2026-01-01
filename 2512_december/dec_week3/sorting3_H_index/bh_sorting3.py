def solution(citations):
    answer = 0
    citations.sort()
    n = len(citations)
    
    for i in range(n):
        h = n - i # h번
        if citations[i] >= h: # 현재 논문의 인용 횟수가 h 번 이상?
            return h
            
    return answer