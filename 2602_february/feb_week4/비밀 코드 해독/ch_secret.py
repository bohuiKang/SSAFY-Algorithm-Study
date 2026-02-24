from itertools import combinations

def solution(n, q, ans):
    answer = 0
    # 모든 조합을 생성해서 분석도구의 결과와 부합하는지 확인
    for candidate in combinations(range(1, n+1), 5):
        # 분석도구에 넣은 번호를 순회
        for i in range(len(q)):
            count = 0
            for x in q[i]:
                if x in candidate:
                    count += 1
            if count != ans[i]:
                break
        # 모든 분석도구의 결과(ans)에 만족하면 가능한 비밀 코드
        else:
            answer += 1
    return answer