import math

def solution(players, m, k):
    answer = 0

    # 기본 구현하고 코너케이스 추가 구현하기

    # 현재 시간별로 돌아가는(돌아갈) 서버 개수
    running_server_num = [0] * 24

    # 0시부터 23시까지 차례로 하기
    for i in range(24):
        # print(players[i])
        # 필요한 서버 개수
        need_server_num = int(math.ceil((players[i] - (m - 1)) / m))

        # 지금 몇 대 더 증설해야 하는지 계산하기
        add_server_num = need_server_num - running_server_num[i]

        # 더 증설해야 하면 증설값 누적하고 그만큼 k 시간대 다 +증설값 하기
        if add_server_num > 0:
            # 증설해야 함
            answer += add_server_num  # 증설값만큼 answer 누적하기

            for j in range(k):
                if i + j < 24:
                    running_server_num[i + j] += add_server_num

    return answer

# print("#1", solution([0, 2, 3, 3, 1, 2, 0, 0, 0, 0, 4, 2, 0, 6, 0, 4, 2, 13, 3, 5, 10, 0, 1, 5], 3, 5))
# print("#2", solution([0, 0, 0, 10, 0, 12, 0, 15, 0, 1, 0, 1, 0, 0, 0, 5, 0, 0, 11, 0, 8, 0, 0, 0], 5, 1))
# print("#3", solution([0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 5, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1], 1, 1))