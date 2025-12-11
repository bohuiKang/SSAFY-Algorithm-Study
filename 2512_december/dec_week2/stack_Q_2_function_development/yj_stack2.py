def solution(progresses, speeds):
    answer = []
    cur = 0  # 스택의 맨 앞 포인터
    while cur < len(progresses): # progresses가 텅 빌때까지 반복
        # 1. 하루 작업량을 보내기 - (progresses - speeds)
        for i in range(cur, len(progresses)):
            progresses[i] += speeds[i]
        # 2. 하루 끝에 작업이 완료된 앞 부분의 기능이 있으면 끝난거 모조리배포하기
        if progresses[cur] >= 100:  # 작업이 완료된 앞 부분의 기능이 있으면
            pop_cnt = 0
            for i in range(cur, len(progresses)):
                if progresses[i] >= 100:  # 작업 완료 시 포인터 뒤로 옮김
                    cur += 1
                    pop_cnt += 1
                else:
                    break
            answer.append(pop_cnt)
    return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))