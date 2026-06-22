def solution(bin1, bin2):
    answer = ''    
    plus = (int(bin1, 2)+int(bin2, 2))  # 2진수를 10진수로 변환
    answer = bin(plus)[2:]  # 10진수를 2진수로 변환
    return answer

print(solution('10', '11'))