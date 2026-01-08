
# total_num = set() 
def get_num(numbers,len_numbers, choose_num_cnt, cnt, use_idx, str_num): # 리스트, 리스트길이, 고를 숫자 개수, 사용한 숫자 인덱스 번호
    global total_num
    
    if cnt == choose_num_cnt: # base case

        if str_num[0] == "0": # 맨 앞이 0 이면 포함 안시킴
            return
        
        str_num = int(str_num) # 그 외는 숫자로 바꾸기
        if str_num == 1: # 1이면 소수 아님
            return
        
        total_num.add(str_num) # set에 넣기
        return 

    for j in range(len_numbers):
        if j in use_idx: # 이미 사용한 숫자는 건너뛰기
            continue
        new_str = str_num + numbers[j]
        get_num(numbers, len_numbers, choose_num_cnt, cnt+1, use_idx + [j], new_str)

def solution(numbers):
    global total_num
    total_num = set()
    answer = 0
    numbers = list(numbers)
    len_numbers = len(numbers)
    for i in range(1, len_numbers+1): # 고를 숫자 개수 정하기 (1개, 2개 .... 전체 개수)
        get_num(numbers, len_numbers, i, 0, [], "") # 숫자 만들어서 set에 넣기
    
    total_num = list(total_num)
    for num in total_num: # 소수인지 판단하기
        for i in range(2, num):
            if num % i == 0: # 2부터 숫자 -1 까지 나눠서 나머지 없으면 소수 아님
                break
        else:
            answer += 1

    return answer

print(solution("17"))
total_num = set() 
print(solution("011"))