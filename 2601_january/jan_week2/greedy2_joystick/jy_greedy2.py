def solution(name):
    answer = 0
    n = len(name)

    # 상하 조작 횟수
    for char in name:
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

    # 좌우 이동 최솟값 찾기
    min_move = n - 1

    # 각 위치에서 오른쪽/왼쪽 선택
    for i in range(n):
        # i까지 오른쪽으로 이동
        next_i = i + 1

        # 연속된 A 건너뛰기
        while next_i < n and name[next_i] == 'A':
            next_i += 1

        # 경로 계산
        # 1) 쭉 오른쪽: n - 1
        # 2) i까지 갔다가 왼쪽: i + i + (n - next_i)
        # 3) 왼쪽 먼저: (n - next_i) + (n - next_i) + i
        min_move = min(
            min_move,
            i * 2 + (n - next_i),
            (n - next_i) * 2 + i
        )

    return answer + min_move