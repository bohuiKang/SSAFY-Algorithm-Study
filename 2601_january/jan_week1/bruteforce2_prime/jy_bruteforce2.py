from itertools import permutations

# 소수인지 확인
def check_prime(n):
    # 0과 1은 소수가 아니니 바로 False return
    if n < 2:
        return False

    # n이 소수인지 알려면 2 ~ n의 제곱근만 나누면 됨
    # n ** 0.5 = n의 제곱근 -> limit까지만 for문을 진행
    limit = int(n ** 0.5)
    for i in range(2, limit + 1):
        # limit + 1까지 중 나눠떨어지는 수가 하나라도 있으면 소수가 아님
        if n % i == 0:
            return False
    # 제곱근에 도달할 때 까지 아무런 수도 없었을 경우 소수이므로 True return
    return True

def solution(numbers):
    answer = 0
    # numbers로 만들 수 있는 숫자들을 집어넣을 set (중복을 피하기 위해)
    numbers_per = set()

    # 종이를 1장 ~ 현재 존재하는 최대 장수까지 뽑음
    for i in range(1, len(numbers) + 1):
        # 순열 생성
        for p in permutations(numbers, i):
            # 만들어진 각 숫자들이 쪼개져있으므로 합쳐서 진짜 숫자로 변환
            num = int("".join(p))
            # 숫자 조합에 집어넣음
            numbers_per.add(num)

    for num in numbers_per:
        # 숫자 조합에 있는 숫자가 소수라면 +1
        if check_prime(num):
            answer += 1

    return answer