clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]

def solution(clothes):
    # 이따 곱셈을 위해 1을 할당
    answer = 1
    # 의상의 종류별 갯수를 세기 위한 딕셔너리, 키-값 : 카테고리-카테고리별 옷의 수
    d = {}
    for cl, ca in clothes:
        d[ca] = d.get(ca, 0) + 1

    # 카테고리별 순회
    for c in d:
        # 각 경우의 수(종류별 옷의 수 + 1 (안 입는 경우))를 곱해준다
        answer *= (d[c] + 1)

    # 아무것도 안 입는 경우를 빼준다
    answer -= 1
    return answer

print(solution(clothes))