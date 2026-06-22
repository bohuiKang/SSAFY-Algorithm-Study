def solution(n, w, num):
    # 빈 컨테이너 구현
    max_row = (n // w) + 1
    if n % w == 0:
        max_row -= 1
    container = [[None] * w for _ in range(max_row)]
    
    # 컨테이너에 박스 삽입
    for i in range(1, n + 1):
        row_num = (i - 1) // w  # 박스가 놓여질 층
        if row_num % 2 == 0: # 홀수 층이면
            container[row_num][(i - 1) % w] = i
        else:   # 짝수 층이면
            container[row_num][(w - 1) - ((i - 1) % w)] = i

    # 꺼낼 박스 위의 상자 개수 반환
    # row_num: 꺼낼 박스가 놓인 층 / col_num: 꺼낼 박스의 인덱스(가로 칸)
    row_num = (num - 1) // w    
    if row_num % 2 == 0:
        col_num = (num - 1) % w
    else:
        col_num = (w - 1) - ((num - 1) % w)
    
    answer = 1
    for row in range(row_num + 1, max_row): # 꺼낼 박스 위 층부터 제일 꼭대기 층까지
        if container[row][col_num] == None:
            break
        answer += 1
        
    return answer
