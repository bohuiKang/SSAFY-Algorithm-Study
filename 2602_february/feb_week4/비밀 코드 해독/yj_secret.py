from itertools import combinations

def solution(n, q, ans):
    answer = 0
    iter = [i for i in range(1, n + 1)]  # 조합 돌릴 범위
    m = len(q)  # 시도 횟수
    # 조합 돌리기
    for combination in combinations(iter, 5):
        # 한 조합(combination)이 q, ans와 모두 일치하는지 확인
        for index in range(m):
            tmp_len = len(set(combination) & set(q[index]))
            if tmp_len != ans[index]:
              break
        else:
            answer += 1

    return answer

# 답은 3, 5가 나와야 함
print(solution(10, [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [3, 7, 8, 9, 10], [2, 5, 7, 9, 10], [3, 4, 5, 6, 7]], [2, 3, 4, 3, 3]))
print(solution(15, [[2, 3, 9, 12, 13], [1, 4, 6, 7, 9], [1, 2, 8, 10, 12], [6, 7, 11, 13, 15], [1, 4, 10, 11, 14]], [2, 1, 3, 0, 1]))

