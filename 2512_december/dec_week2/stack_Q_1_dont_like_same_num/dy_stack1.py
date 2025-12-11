def solution(arr):
    answer=[]
    # 직전값 변수, 숫자는 1~9까지니까 10 할당
    prev = 10
    for a in arr:
        # 전체 순회, 직전값과 같지 않다면 정답에 넣고, 직전값 갱신
        if prev != a:
            answer.append(a)
            prev = a
    return answer