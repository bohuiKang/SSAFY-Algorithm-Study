import heapq

def solution(operations):
    answer = []
    
    hq_list = []
    for opers in operations:
        oper = opers.split(" ")
        order, num = oper
        num = int(num)
        if order == 'I':
            heapq.heappush(hq_list, num)
        elif order == 'D':
            if num == 1: # 최댓값
                hq_temp = []
                if hq_list: # 있으면,
                    for _ in range(len(hq_list) - 1):
                        n = heapq.heappop(hq_list)
                        heapq.heappush(hq_temp, n)
                    hq_list = hq_temp
            elif num == -1: # 최솟값
                if hq_list: # 있으면
                    heapq.heappop(hq_list)        

    if hq_list: # 있으면,
        if len(hq_list) > 1:
            min_num = heapq.heappop(hq_list) 
            max_num = 0
            while hq_list: 
                max_num = heapq.heappop(hq_list)
            answer.append(max_num)
            answer.append(min_num)
        else: # 하나만 남으면,
            one_num = heapq.heappop(hq_list) 
            answer = [one_num, one_num]
    else: # 없으면,
        answer = [0, 0]
        
    return answer

print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))