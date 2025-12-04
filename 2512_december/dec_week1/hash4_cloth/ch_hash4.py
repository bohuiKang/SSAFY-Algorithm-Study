def solution(clothes):
    hsh = {}
    for clothe in clothes:
        hsh.setdefault(clothe[1], []).append(clothe[0])
    answer = 1
    for key in hsh:
        answer *= (len(hsh[key]) + 1)
    return answer - 1  # 옷을 모두 다 안 입는 경우 제외