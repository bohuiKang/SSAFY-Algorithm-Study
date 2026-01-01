def solution(citations):
    answer = 0
    # 내림차순 정렬
    citations.sort(reverse=True)
    
    for i in range(len(citations)):
        if citations[i] < i + 1:  # 논문 인용 h번 미만
            return i  # h-index
        
    # [10, 10, 10]
    return len(citations)