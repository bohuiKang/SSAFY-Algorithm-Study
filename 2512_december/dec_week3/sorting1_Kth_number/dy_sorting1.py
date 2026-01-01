def solution(array, commands):
    answer = []
    # 작업의 수
    n = len(commands)
    # 모든 작업을 수행할때까지 반복
    for i in range(n):
        start, last, target = commands[i]
        # 원하는 배열을 잘라 따로 저장
        lst = array[start-1:last]
        # 정렬
        lst.sort()
        # 해당하는 숫자를 answer에 따로 저장
        answer.append(lst[target-1])
        
    return answer