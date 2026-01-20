def solution(name):
    answer = 0
    N = len(name)

    move = N - 1
    for idx in range(N):      
        # 상하 이동 알파벳 변경
        gap = ord(name[idx]) - ord('A')
        if gap > 13: # 뒤로 이동하는게 더 가까울 때
            answer += (gap - 26) * (-1)
            # print(f'{name[idx]} => {(gap - 26) * (-1)}')
        else:
            answer += gap
        
        # 좌우 위치 이동
        next_idx = idx + 1
        print(f'{name[idx]} / {idx} => ', end='')
        # A가 아닌 알파벳의 인덱스를 찾음 => AAA 연속 구간이 여러개 있을 때, 하나의 연속 구간만 피할 수 있다. 
        while next_idx < N and name[next_idx] == 'A':
            print(f'{name[next_idx]},', end='')
            next_idx += 1
        print(f' = {next_idx}')
        d_to_forward = idx
        d_to_backward = N - next_idx

        path_turn_right = d_to_forward * 2 + d_to_backward
        path_turn_left = d_to_backward * 2 + d_to_forward

        move = min(move, path_turn_right, path_turn_left)

    return answer + move

print(solution('JAZ')) # 11
# print(solution('JAN')) # 23
# print(solution('JEROEN')) # 56
# print(solution('ZAZAZ')) # 6
# print(solution('ZAZA')) # 4

# 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# '01234567890123210987654321'