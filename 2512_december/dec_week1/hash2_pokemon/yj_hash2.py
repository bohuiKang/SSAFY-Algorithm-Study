from collections import Counter

def solution(nums):
    N = len(nums)
    counter = Counter(nums)
    if len(counter) >= N / 2:  # 종류 개수 >= 고를 수 있는 수
        return N / 2  # 최대로 폰켓몬 고름
    else:  # 종류 개수 < 고를 수 있는 수
        return len(counter)  # 종류만큼 폰켓몬 고름