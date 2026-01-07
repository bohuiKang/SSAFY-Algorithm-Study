'''
def solution(answers):
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]

    scores = []
    for pattern in patterns:
        score = 0
        for i in range(len(answers)):
            if pattern[i % len(pattern)] == answers[i]:
                score += 1
        scores.append(score)

    max_score = max(scores)
    return [i + 1 for i in range(len(scores)) if scores[i] == max_score]
'''

def solution(answers):
    # 최고 득점자 명단
    answer = []
    # 문제의 수
    n = len(answers)
    # 최고 점수
    max_score = 0

    score = 0
    # 1번 사람
    for i in range(n):
        # i % 5는 0~4를 반복하므로, +1 하여 1~5를 반복
        if i % 5 + 1 == answers[i]:
            score += 1

    # 1번 수포자가 첫 번째이므로 무조건 최고 득점자에 포함
    # 최고 점수 갱신
    max_score = score
    # 최고 득점자 명단에 추가
    answer.append(1)
    # 점수 초기화
    score = 0

    # 2번 사람
    flag = 0
    # 짝수 인덱스(0, 2, 4, ...)는 항상 2
    # 홀수 인덱스(1, 3, 5, ...)는 1, 3, 4, 5를 순서대로
    for i in range(n):
        # 짝수 번째 문제
        if i % 2 == 0:
            if answers[i] == 2:
                score += 1
        else:
            # flag 값에 따라 1, 3, 4, 5 중 하나와 비교
            if flag == 0:
                if answers[i] == 1:
                    score += 1
            elif flag == 1:
                if answers[i] == 3:
                    score += 1
            elif flag == 2:
                if answers[i] == 4:
                    score += 1
            elif flag == 3:
                if answers[i] == 5:
                    score += 1
                # flag 초기화, 다음 증가 후 0이 되도록 -1로 설정
                flag = -1
            # 다음 홀수 인덱스를 위해 flag 증가
            flag += 1

    # 최고 점수 갱신
    if max_score < score:
        # 최고 점수보다 더 높으면 명단 갱신
        max_score = score
        answer = [2]
    # 같다면 명단에 추가
    elif max_score == score:
        answer.append(2)
    # 점수 초기화
    score = 0

    # 3번 사람
    # 각 숫자가 2번씩 반복됨
    lst = [3, 1, 2, 4, 5]
    flag = 0
    for i in range(n):
        if i % 2 == 0:
            if answers[i] == lst[flag]:
                score += 1
        else:
            # 직전 답안과 같은 답안 제출
            if answers[i] == lst[flag]:
                score += 1
            # 이후에는 다음 답안으로 갱신
            flag = (flag+1) % 5

    # 최고 점수 갱신
    if max_score < score:
        max_score = score
        answer = [3]
    elif max_score == score:
        answer.append(3)

    return answer