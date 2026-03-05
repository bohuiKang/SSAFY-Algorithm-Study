from collections import deque

def solution(players, m, k):
    answer = 0
    now_server = 0
    time = deque([(0,0)])
    for player in players:

        if player // m > now_server:
            diff = (player // m) - now_server
            answer += diff
            now_server += diff
            time.append((k-1, diff))

        len_time = len(time)
        for i in range(len_time):
            time_check, server_check = time.popleft()
            if time_check - 1 <= 0:
                now_server = now_server - server_check


    return answer


