from itertools import permutations

# 소수인지 판별하는 함수
def is_prime(num):
    # 0, 1은 소수가 아님
    if num < 2:
        return False
    # 2는 소수
    if num == 2:
        return True
    # 짝수 제외
    if num % 2 == 0:
        return False

    # 2부터 num-1까지 나누어떨어지는 수가 있는지 확인
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    # 문자열을 리스트로 변환 (각 자리 숫자 분리)
    numbers = list(numbers)
    # 숫자의 개수
    n = len(numbers)
    # 만들 수 있는 모든 숫자를 저장할 set (중복 제거)
    num_lst = set()
    # 소수의 개수
    answer = 0

    for i in range(1, n+1):
        # 1자리부터 n자리까지 모든 순열 생성
        for per in permutations(numbers, i):
            # 생성된 모든 순열을 공백없이 더한후 set에 추가
            num_lst.add(int("".join(per)))

    # 만들어진 set을 하나씩 소수인지 확인
    for s in num_lst:
        if is_prime(s):
            answer += 1

    return answer