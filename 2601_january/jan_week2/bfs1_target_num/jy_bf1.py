def solution(numbers, target):
    answer = 0

    def recur(cnt, current):
        nonlocal answer

        if cnt == len(numbers):
            if current == target:
                answer += 1
            return

        recur(cnt + 1, current + numbers[cnt])
        recur(cnt + 1, current - numbers[cnt])

    recur(0, 0)
    return answer