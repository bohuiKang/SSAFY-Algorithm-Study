def solution(answers):

    # 각 학생들의 패턴
    patterns = [1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    # 각 학생들의 점수를 기록해둘 리스트
    scores = [0, 0, 0]

    # enumerate를 통해 인덱스와 값을 동시에 받아옴
    for i, answer in enumerate(answers):
        for j, pattern in enumerate(patterns):
            # answer = 각 문제의 정답
            # pattern[i % len(pattern)] = 학생이 적어낸 정답
            # 듈이 같다면 == 정답이라면 학생 인덱스에 +1
            if answer == pattern[i % len(pattern)]:
                scores[j] += 1

    answer = []
    # 가장 점수가 높은 학생을 출력할 것이기에 max값을 산출해냄
    max_score = max(scores)
    for i in range(len(scores)):
        # 최댓값과 같다면
        if scores[i] == max_score:
            # answer에 i+1만큼 추가해줌 -> 오름차순으로 정렬 가능
            answer.append(i+1)

    return answer