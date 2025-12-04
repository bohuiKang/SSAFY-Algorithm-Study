def solution(participant, completion):
    # 이름 순대로 정렬
    participant.sort()
    completion.sort()
    # 다르면 컷
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    # 끝까지 같으면 participant에서 남은 사람이 미완주자
    return participant[-1]