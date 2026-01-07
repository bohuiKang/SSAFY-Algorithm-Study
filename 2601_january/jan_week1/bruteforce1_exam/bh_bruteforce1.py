def solution(answers):
    right_arr = [0] * 3 # 맞춘 횟수 저장 리스트 변수
    answer = [] # 가장 높은 점수 받은 사람(들) 저장 리스트 변수
    n = len(answers)
    math_losers = ['12345', '21232425', '3311224455']
    
    for idx, loser in enumerate(math_losers):
        check_ans = loser * (n // len(loser) + 1) # 정답 길이 만큼 수포자 찍기번호 늘리기
        cnt = 0
        for i in range(n): # 정답 길이 만큼 for 문
            if int(check_ans[i]) == answers[i]: 
                cnt += 1
        
        right_arr[idx] = [cnt, idx] # 맞춘 개수와 순서 저장
    
    right_arr.sort(reverse=True) # 맞춘 개수가 많은 순으로 정렬
    max_cnt = right_arr[0][0]

    for same_check, idx in right_arr: # max 값이 여러개인 경우 체크
        if max_cnt == same_check:
            answer.append(idx +1) # 인덱스 번호에 +1 (0번 인덱스 = 첫번째 요소)
        else:
            break

    answer.sort() # 오름차순 정렬
    return answer


print(solution([1,3,2,4,2]))