def solution(participant, completion):
    answer = ''
    par_dic = {}
    for player in participant:
        if player in par_dic:
            par_dic[player] += 1
        else:
            par_dic[player] = 1

    for player in completion:
        par_dic[player] -= 1

    for player in participant:
        if par_dic[player]:
            answer = player
            return answer
# 딕셔너리는 해시값으로 접근 list는 index로 접근 시간 차이가 나게 됨
# hash는 메모리를 더쓰지만 시간 복잡도가 낮다.