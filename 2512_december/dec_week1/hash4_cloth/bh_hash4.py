from collections import defaultdict

def solution(clothes):
    answer = 1
    cloth_type = defaultdict(int)
    for cloth, c_type in clothes:
        cloth_type[c_type] += 1
    
    for k, v in cloth_type.items():
        answer *= (v+1)

    return answer - 1