# 시간 초과가 날 줄 알아 어려운 길로 갔으나
# 돌아와 해보니 의외로 시간 초과가 나지 않음
# 가장 간단한 코드가 가장 잘 짠 코드다 ...

def solution(n):
    for x in range(2, n):
        if n % x == 1:
            return x