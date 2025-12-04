# 경우의 수 식 이용 각 의상 종류 해당 개수 + 1 을 다 곱한뒤 -1
# 지금 생각해보니 그냥 숫자만 넣어서 해도 되었겠다 딕셔너리 이름넣어서 괜히 만들었네
clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
def solution(clothes):
    
    cloth_dic = {}
    for cloth in clothes:
        if cloth[1] not in cloth_dic:
            cloth_dic[cloth[1]] = [cloth[0]]
        else:
            cloth_dic[cloth[1]] += [cloth[0]]

    answer = 1
    for cloth in cloth_dic:
        answer *= (len(cloth_dic[cloth])+1)
    
    answer -= 1
    return answer

print(solution(clothes))