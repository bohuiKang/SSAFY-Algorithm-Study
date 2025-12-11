progresses = [93, 30, 55]	
speeds = [1, 30, 5]

def solution(progresses, speeds):
    answer = []
    days = len(progresses)
    day_list = [0] * days

    for i in range(days): # 각 개발이 얼마나 걸리는지 계산해서 담기
        left_day = 100 - progresses[i]
        speed = speeds[i]
        if left_day % speed :
            finish_day = (left_day // speed) + 1
        else:
            finish_day =  left_day // speed
        day_list[i] = finish_day
    
    pre_finish = day_list.pop(0) 
    while day_list:
        cnt = 1
        while day_list:
            next_finish = day_list.pop(0)
            if next_finish > pre_finish:
                pre_finish = next_finish
                answer.append(cnt)
                cnt = 1 # 마지막에 1개 남은 경우 넣어주기 위해서 (pop 미리 해서 비어버려서 마지막은 while 안돌게됨)
                break

            cnt += 1
    
    answer.append(cnt) # 마지막 날짜는 day_list가 비어있어서 while 안돌아서 넣어줘야함
    
    return answer

print(solution(progresses, speeds))