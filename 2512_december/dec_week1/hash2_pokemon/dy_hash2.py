def solution(nums):
    answer = 0
    # 선택할 수 있는 폰켓몬의 수
    c = len(nums)/2
    # 폰켓몬의 종류 수
    n = len(set(nums))
    # 가져갈 수 있는 종류는 두 값 중 더 작은 값
    answer = min(c, n)
    return answer

