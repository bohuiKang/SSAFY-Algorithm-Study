def solution(bin1, bin2):
    # int: 2진수 문자열을 10진수 정수로 변환
    # bin: 그걸 다시 2진수로 변환
    # 그런데 2진수 문자열로 변환 시 앞에 0b가 붙어서 슬라이싱(2:)
    answer = bin(int(bin1, 2) + int(bin2, 2))[2:]
    return answer