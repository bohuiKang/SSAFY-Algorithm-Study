def solution(bin1, bin2):
    # 2진수로 변환
    b1 = int(bin1, 2)
    b2 = int(bin2, 2)
    # 값을 더한 후 다시 2진수 변환
    answer = format(b1+b2, 'b')
    return answer