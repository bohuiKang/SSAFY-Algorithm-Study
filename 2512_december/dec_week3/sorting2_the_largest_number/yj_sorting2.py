def solution(numbers):
    answer = ''
    # 쿤자열로 바꾸기
    numbers = list(map(str, numbers))
    
    # 각 number를 세 번 곱하고 비교해서 내림차순 정렬 (1,000 이하인걸 활용)
    numbers.sort(key=lambda x: x * 3, reverse=True)
    
    # 정렬된 숫자 하나로 합치기
    answer = answer.join(numbers)
    
    # 정답이 0인 경우
    return str(int(answer))