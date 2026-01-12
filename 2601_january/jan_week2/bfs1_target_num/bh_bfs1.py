def solution(numbers, target):
    N = len(numbers)
    
    def recur(total, idx):
        if idx == N:
            if total == target:
                return 1
            return 0
        
        return recur(total + numbers[idx], idx + 1) + recur(total - numbers[idx], idx + 1)

    return recur(0, 0) # total, idx 위치 값

print(solution([1, 1, 1, 1, 1], 3))