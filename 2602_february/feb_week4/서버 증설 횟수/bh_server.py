# m명당 서버 1개

def solution(players, m, k): # 시간별 이용자 수, 서버 감당 이용자 수, 추가 서버 유지 시간
    answer = 0 # 추가로 서버 증설한 개수 저장 변수
    server_list = [0] * 24 # 증설된 서버 관리 리스트

    # 1. 시간별 사용자를 기준으로 서버 증설 필요 확인
    for time in range(len(players)): # 0 ~ 23
        servers = players[time] // m    # 필요한 서버 개수 확인
        # 2. server_list에서 해당 시간의 서버 개수 확인
        if server_list[time] < servers: # 필요한 서버 개수보다 지금 서버 개수가 작을 때
            needs = servers - server_list[time]
            answer += needs

            # 3. 서버 개수가 부족하면 지금시간부터 k시간까지 server_list에 +(필요한 추가 서버)
            for expan in range(time, time + k):
                if expan < 24:  # 하루를 초과하는 서버 시간은 제외
                    server_list[expan] += needs
    return answer

print('# 1 => ', solution([0, 2, 3, 3, 1, 2, 0, 0, 0, 0, 4, 2, 0, 6, 0, 4, 2, 13, 3, 5, 10, 0, 1, 5], 3, 5))
print('# 2 => ', solution([0, 0, 0, 10, 0, 12, 0, 15, 0, 1, 0, 1, 0, 0, 0, 5, 0, 0, 11, 0, 8, 0, 0, 0], 5, 1))
print('# 3 => ', solution([0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 5, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1], 1, 1))
