# N 마리의 폰켓몬 중에서 N/2마리를 가져가도 좋다
# 4마리의 폰켓몬 중 2마리를 고르는 방법은 6가지
# 가질 수 있는 폰켓몬 종류 수의 최댓값은 2
# 최대한 많은 종류의 폰켓몬을 선택하는 방법을 찾아, 
# 그때의 폰켓몬 종류 번호의 개수를 return
# nums의 길이(N)는 1 이상 10,000 이하의 자연수이며, 항상 짝수
def solution(nums):
    answer = 0

    half = len(nums) // 2
    total = len(set(nums))
    
    if half <= total:
        answer = half
    elif half > total:
        answer = total
        
    return answer