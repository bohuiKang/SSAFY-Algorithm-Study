def solution(bin1, bin2):
    #  1. bin1, 2를 십진수 정수로 변환 -> int(bin1, 2), int(bin2, 2)
    #  2. 1끼리의 합을 다시 이진수로 변환, bin()의 return 값은 str
    #  3. 2의 '0b'값 제거를 위해 슬라이싱 -> [2:]
    return bin(int(bin1, 2) + int(bin2, 2))[2:]