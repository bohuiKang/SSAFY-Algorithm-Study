def solution(number, k):
    answer = ''
    number = list(number)
    len_number = len(number)
    reverse_k = len_number - k
    max_val = 0

    def make_num(idx, cnt, answer): # 지금까지 확인한 인덱스, 고른 개수
        nonlocal max_val

        if reverse_k - cnt > len_number - idx:
            return
        if cnt == reverse_k:
            max_val = max(int(answer), max_val)
            return
        
        if idx == len_number:
            return
        
        for i in range(idx, len_number):
            new_answer = answer + number[i]
            make_num(i+1, cnt+1, new_answer)
    make_num(0, 0, "")
    return str(max_val)

print(solution("1924", 2))
print(solution("1231234",3))