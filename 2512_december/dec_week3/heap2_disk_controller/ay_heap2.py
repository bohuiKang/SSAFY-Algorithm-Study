import heapq as hq

def solution(jobs):
    answer = 0
    wait = []
    task_num = len(jobs)
    return_time = [0]*task_num
    idx = 0
    time = 0
    hq.heapify(jobs)
    
    while jobs or wait: # 진행할 작업이 남아있을 동안 돌림

        while jobs:

            input_time, task_length = hq.heappop(jobs)

            if input_time <= time:
                hq.heappush(wait,[task_length, input_time])
            else:
                hq.heappush(jobs, [input_time, task_length])
                break

        if wait: # 대기큐에 작업시킬 애들 있으면 작동, 이 작업은 while을 돌리면 안됨 작업 한번 처리하고 다시 대기큐에 들어간 애들이 달라지기 때문
            task = hq.heappop(wait)
            time += task[0]
            return_time[idx] = time - task[1]
            idx += 1
        else:
            time += 1
    
    answer = sum(return_time) // task_num

    return answer
    

print(solution([[0, 3], [1, 9], [3, 5]]))