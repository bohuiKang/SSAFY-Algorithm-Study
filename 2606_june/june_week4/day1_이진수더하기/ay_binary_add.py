def solution(bin1, bin2):
    answer = ''
    len_1 = len(bin1)
    len_2 = len(bin2)
    max_len = max(len_1, len_2) # 최대 자릿수는 최장 자리수 + 1까지만 가능

    if max_len == len_1:
        bin2 = ((len_1 - len_2) * "0") + bin2 
    else:
        bin1 = ((len_2 - len_1) * "0") + bin1 
    max_len += 1
    bin1 = "0" + bin1
    bin2 = "0" + bin2
    digit = [0] * max_len

    for i in range(max_len-1, -1, -1):
        num = int(bin1[i]) + int(bin2[i]) + digit[i]

        if num >= 2: # 2보다 크면 2를 빼준 값만큼 그자리에 들어감 윗 자리로 올려줘야함
            digit[i] = num - 2
            digit[i-1] = 1
        else:
            digit[i] = num
    
    result = digit

    if len(digit) != 1 and digit[0] == 0:
        result = digit[1:]
    
    
    for num in result:
        answer += str(num)

    return answer

print(solution("10", "11"))