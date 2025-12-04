def solution(participant, completion):
    dic = {}
    for i in completion:
        dic.setdefault(i, 0)
        dic[i] += 1
    for j in participant:
        if j not in dic:
            return j
        dic[j] -= 1
        if dic[j] < 0:
            return j