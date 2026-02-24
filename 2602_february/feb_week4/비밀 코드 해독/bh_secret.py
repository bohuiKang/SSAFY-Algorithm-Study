# 1~n개 5개 오름차순 비밀 코드 (n은 10~30)
# m번 시도 -> 몇개 일치인지 반환 (q=m은 1~10)
# 비밀 코드로 가능한 정수 조합 개수 확인

from itertools import combinations

def solution(n, q, ans):
    nums = set(i for i in range(1, n+1))
    candi_list = [] # 각 case에 대한 후보 리스트 저장

    for i in range(len(q)):
        candi_list.append(candidates(nums, q[i], ans[i]))

    # candi_list의 교집합으로 출력된 개수
    intersection = candi_list[0]
    for i in range(1, len(candi_list)):
        intersection &= candi_list[i]

    return len(intersection)


def candidates(nums, case, right): # 시도한 case, 일치 개수
    # right 개를 포함하고 (5 - right)개를 제외한 나머지 값으로 후보 조합 만들기
    others = nums - set(case)
    # print(others)
    candi_right = list(combinations(case, right))
    candi_other = list(combinations(others, 5 - right))
    this_candi  = set()
    for i in candi_right: # 조합을 위한 2중 for문
        for j in candi_other:
            this_candi.add(tuple(sorted(i + j)))
    # print(this_candi)
    return this_candi



# 아니면 ans 값이 제일 큰 케이스 하나를 선택해 후보 조합을 생성하고 하나씩 돌려보기? => 이게 맞는 듯

print(solution(10, [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [3, 7, 8, 9, 10], [2, 5, 7, 9, 10], [3, 4, 5, 6, 7]], [2, 3, 4, 3, 3]))