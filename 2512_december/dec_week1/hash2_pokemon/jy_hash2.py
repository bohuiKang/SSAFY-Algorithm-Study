def solution(nums):
    # len(set(nums)) -> 포켓몬 종류 수
    # len(nums)//2) -> 내가 가져갈 수 있는 포켓몬 수
    # 최대한 선택 가능한 수와 서로 다른 종류 수 중 더 작은 쪽이 정답
    # 뽑을 수 있는 수 < 종류 -> 종류 다 못 담음 / 뽑을 수 있는 수 > 종류 -> 종류 전체가 최대
    return min(len(set(nums)), len(nums)//2)

