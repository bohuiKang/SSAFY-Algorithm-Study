def solution(players, m, k):
    # 서버 증설 된 횟수
    answer = 0
    # 증설 서버 관리 리스트
    s_l = [0]*24

    # 서버 증설 시 (증설 시작 시간대, 증설 개수)
    def add_s(start, n):
        # 함수 내부에서 변수를 찾는 것이기에 global이 아닌 nonlocal
        nonlocal answer

        # 증설 횟수 증가
        answer += n

        # 관리 리스트 업데이트
        for i in range(start, start+k):
            if i >= 24:
                break
            s_l[i] += n

        return

    # now: 현재 시간대
    for now in range(24):
        # 현재 시간대의 이용자 수
        now_player = players[now]
        # 현재 서버의 수
        now_s = s_l[now] + 1
        # 현재 이용자 수를 감당하기 위한 서버의 수
        p_p = now_s*m
        # 현재 서버가 이용자 수를 감당 불가능하다면
        if now_player >= p_p:
            # 증설해야되는 수
            num = (now_player - p_p) // m + 1
            # 현재시간대부터 num개 증설
            add_s(now, num)

    return answer

print(solution([0, 2, 3, 3, 1, 2, 0, 0, 0, 0, 4, 2, 0, 6, 0, 4, 2, 13, 3, 5, 10, 0, 1, 5], 3, 5))
