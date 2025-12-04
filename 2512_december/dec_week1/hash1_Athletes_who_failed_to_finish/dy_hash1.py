def solution(participant, completion):
    # 마라톤 선수 목록 딕셔너리, 키-값: 이름-인원수
    d = {}
    answer = ''
    for p in participant:
        '''
        # 값이 없으면 키 생성, 값에 0을 할당
        d.setdefault(p, 0)
        # 값 1 증가
        d[p] += 1
        '''
        # 키가 없다면 get이 default=0 반환, 기본값 0 + 1 해서 1 저장
        d[p] = d.get(p, 0) + 1

    for c in completion:
        # 완주목록에서 한명씩 가져와 인원수 감소
        d[c] -= 1
    for p in participant:
        # 인원수가 1명 남았다면 출력
        if d[p] == 1:
            answer = p
            break
    return answer

print(solution(["leo", "kiki", "eden"],["eden", "kiki"] ))