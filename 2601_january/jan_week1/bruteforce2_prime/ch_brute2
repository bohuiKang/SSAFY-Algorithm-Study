from math import isqrt
def solution(numbers):
    N = len(numbers)
    arr = list(map(str, numbers))   # arr: 숫자들이 한개씩 들어있는 배열
    visited = [0] * N
    prime_num = set()
    # 가능한 숫자의 순열을 찾는 함수
    def recur(path):
        if path:    # 길이가 1 이상일때 소수인지 검사
            if is_prime(path):
                prime_num.add(int(path))
        if len(path) == N:
            return
        for i in range(N):
            if visited[i]:
                continue
            visited[i] = 1
            recur(path + arr[i])
            visited[i] = 0

    # 소수인지 판별하는 함수
    def is_prime(path):
        num = int(path)
        # 2부터 num의 제곱근까지 num을 나눠보고 나누어떨어지는 수가 없으면 소수
        if num < 2:  # 1은 소수가 아님
            return 0
        divisor = 0  # 약수 개수
        for n in range(2, isqrt(num) + 1):
            if num % n == 0:
                divisor += 1
        if divisor == 0:
            return 1
        return 0

    recur('')
    return len(prime_num)
