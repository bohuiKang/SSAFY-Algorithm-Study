def solution(clothes):
    answer = 1
    cloth_hash = {}
    # 종류별 의상 수 저장
    for cloth in clothes:
        if cloth[1] in cloth_hash:  # 이미 딕셔너리에 있으면 value += 1하기
            cloth_hash[cloth[1]] += 1
        else:  # 딕셔너리에 없으면 키, 값 추가하기
            cloth_hash[cloth[1]] = 1
            
    # 모든 경우의 수 - 아무것도 안 입은 수 1
    numbers = list(cloth_hash.values())
    for num in numbers:
        answer *= num + 1
    
    answer -= 1
    
    return answer