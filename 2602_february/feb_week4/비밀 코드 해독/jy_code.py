'''
정수들은 오름차순으로 짜여있음
ans가 0인 경우는 없다 ... 아쉽네 그러면 개꿀인데.

시스템 응답이 가장 높았던 걸 기준으로 삼음
시스템 응답이 높았던 걸 기준으로 combination을 만듦
예를 들어 ans=4였으면 combination도 개수를 4개로 지정해서
그런 다음에는 ans가 많은 것들부터 봐봄
위에처럼 combination 만들어서 지금 쌓인 combination이랑 합침
만약 n(combination) < 5면 통과 + 합침 (set으로)
그래서 마지막에 다다랐을 때 n(combination) == 5이면 pass
'''

from itertools import combinations

'''
아니면 n 줬으니까 그걸로 combination 싹~ 다 만들어서
맞는지 검증하면?
'''

def solution(n, q, ans):
    # (응답, 해당배열) 쌍으로 묶어놓음
    data = []
    for i in range(len(ans)):
        data.append((ans[i], set(q[i])))

    # combination을 만들기 위한 숫자들
    base = range(1, n + 1)
    # 이게 결과 (answer)
    result = set()

    # 될 수 있는 후보군들을 모두 만들어놓음
    candidate_lst = set(combinations(base, 5))

    # 후보군들 내의 각각의 후보군을 확인
    for candidate in candidate_lst:
        # 후에 교집합을 위해 set으로 처리
        candidate_set = set(candidate)
        # 조건에 부합하는지 확인하는 flag
        possible = True

        for current_ans, current_q in data:
            # 만약 현재 후보군과 답변의 교집합이 해당 답변의 answer와 같지 않을 경우
            if len(candidate_set & current_q) != current_ans:
                # 조건을 부합하지 못했으므로 False 처리 후 break
                possible = False
                break
        # 아니면 추가
        if possible:
            result.add(candidate)

    return len(result)

