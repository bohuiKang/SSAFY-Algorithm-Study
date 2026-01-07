# 만들어진 숫자 중 몇개가 소수인가? 
# 2~(n의 제곱근까지) 나누기로 소수 확인 or 나누는 값의 제곱이 n보다 크면 중지

import math

def solution(numbers):
    making_n = set() # 숫자 조합을 저장할 변수
    answer = 0

    # 1. 숫자 조합 만드는 내부 함
    def make_number(numbers, idx_arr, making): 
        making_n.add(int(making)) # 만들어진 조합 set에 저장

        if len(making) == len(numbers): # 만들어진 숫자가 제공된 숫자의 길이와 같을 때,
            return
        
        for i in range(len(numbers)):
            if i in idx_arr: # 조합시 내 인덱스는 제외
                continue
            make_number(numbers, idx_arr+[i], making+numbers[i])
        return
    
    # 2. 소수 찾는 함수
    def check_prime(number): 
        divisor = int(math.sqrt(number)) # 제곱근 값 구하기
        
        for n in range(2, divisor + 1):
            if number % n == 0:
                return 0
        return 1 # 나누어 지는 값이 없으므로 number은 소수!

    for idx in range(len(numbers)): # 숫자 조합 함수 호출
        make_number(numbers, [idx], numbers[idx]) # 숫자, 사용한 위치 값 리스트, 숫자

    for n in making_n: # 소수 확인 함수 ghcnf
        if n > 1:
            answer += check_prime(n) 
    return answer

print(solution("011"))