def solution(participant, completion):
    # participant 참여 선수 이름 배열 
    # completion 완주 선수 이름 배열
    participant = sorted(participant)
    completion = sorted(completion)
    
    answer = ''
    # completion의 길이는 participant의 길이보다 1 작습니다.
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
    else:
        answer = participant[len(completion)]        
    
    return answer