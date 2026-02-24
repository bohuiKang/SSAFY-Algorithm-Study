from itertools import combinations


# 부합하는지 확인하는 함수
def check(q_lst, ans, comb):
    # 모든 시도를 검증
    for i in range(len(q_lst)):
        # 현재 조합과 시도의 교집합 개수
        matched = len(set(comb) & set(q_lst[i]))

        # 시스템 응답과 다르면 False 반환
        if matched != ans[i]:
            return False

    # 모든 시도를 통과하면 True
    return True


def solution(n, q, ans):
    answer = 0
    # 1부터 n까지 중 5개를 선택하는 모든 조합을 생성
    lst = combinations(range(1, n + 1), 5)

    # 각 조합을 검증
    for comb in lst:
        # 유효한 조합이면 카운트 증가
        if check(q, ans, comb):
            answer += 1

    return answer