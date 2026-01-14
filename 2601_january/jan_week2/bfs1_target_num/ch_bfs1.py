# 각 칸에서 - or + 선택 후 다음 depth로 재귀
# 기저조건 : 마지막 칸까지 가면 타겟 넘버와 비교 후 return
def solution(numbers, target):
    
    def recur(total, idx):
        nonlocal answer
        if idx == len(numbers):
            if total == target:
                answer += 1
            return

        for i in range(2):
            if i == 0:
                recur(total + numbers[idx], idx + 1)
            else:
                recur(total - numbers[idx], idx + 1)
            
    answer = 0
    recur(0, 0)
    return answer