'''
각 의상 종류가 n개 있으면 종류를 안 입는 경우까지 해서 n + 1
각 종류마다 (n1 + 1) * (n2 + 1) * (n3 + 1) ...
근데 그러면 아무것도 안 입는 경우 존재하니 전체 결과에서 -1
이게 맞나
'''

def solution(clothes):
    clothes_dict = {}

    for name, type in clothes:
        # 종류별 개수 하나씩 추가
        clothes_dict[type] = clothes_dict.get(type, 0) + 1

    answer = 1
    for i in clothes_dict:
        # 각 종류마다 (n1 + 1) * (n2 + 1) * (n3 + 1) ...
        answer *= (clothes_dict[i] + 1)

    return answer - 1