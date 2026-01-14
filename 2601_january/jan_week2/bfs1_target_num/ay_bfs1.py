def solution(numbers, target):

    last_idx = len(numbers)
    cnt = 0

    def dfs(idx, now_sum, last_idx, target):
        nonlocal cnt

        if idx == last_idx: # base case
            if now_sum == target: # target이랑 같으면 cnt+1
                cnt += 1

            return # 조건 만족 안하면 그냥 빠져나옴
        
        next_sum = now_sum + numbers[idx]
        dfs(idx+1, next_sum, last_idx, target)
        next_sum = now_sum - numbers[idx]
        dfs(idx+1, next_sum, last_idx, target)

    dfs(0, 0, last_idx, target)
    return cnt


print(solution([1, 1, 1, 1, 1], 3))