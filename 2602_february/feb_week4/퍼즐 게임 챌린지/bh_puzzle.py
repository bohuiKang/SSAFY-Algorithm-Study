# def solution(diffs, times, limit):

#     left_level = 1
#     right_level = max(diffs)
#     check_time = 0

#     while left_level != right_level:
#         mid_level = (left_level + right_level) // 2

#         check_time = play_puzzle(mid_level, diffs, times, limit)

#         if limit >= check_time: # 제한시간보다 작거나 같을 때
#             right_level = mid_level

#         elif limit < check_time: # 제한시간보다 클 때
#             left_level = mid_level +1

#     return right_level

# def play_puzzle(level, diffs, times, limit):
#     time = 0

#     for i in range(len(diffs)):
#         if diffs[i] <= level: # level이 클 때
#             time += times[i]
#         elif diffs[i] > level: # 난이도가 클 때
#             if i == 0: # 첫 퍼즐일 때,
#                 time += times[i] * (diffs[i] - level ) + times[i]
#             else: 
#                 time += (times[i] + times[i-1]) * (diffs[i] - level) + times[i]
#         if limit < time: # 가지치기, limit를 넘은 level의 time은 끝까지 계산 안하고 리턴
#             return time

#     return time

## ----------------최적화------------------ ##
# 함수를 호출하는 비용이 작지 않다. 

def solution(diffs, times, limit):
    left_level = 1
    right_level = max(diffs)

    while left_level != right_level:
        mid_level = (left_level + right_level) // 2

        possible = True
        check_time = 0
        for i in range(len(diffs)):
            if diffs[i] <= mid_level:   # level이 클 때   
                check_time += times[i]
            elif diffs[i] > mid_level:  # 난이도가 클 때
                prev_time = times[i-1] if i > 0 else 0 # i가 0일 때의 로직 처리
                check_time += (times[i] + prev_time) * (diffs[i] - mid_level) + times[i]
        
            if limit < check_time: # 가지치기, limit를 넘은 level의 time은 끝까지 계산 안하고 리턴
                possible = False
                break
        
        if possible:    # 제한시간보다 작거나 같을 때
            right_level = mid_level
        else:           # 제한시간보다 클 때
            left_level = mid_level +1

    return right_level


print(solution([1, 5, 3], [2, 4, 7], 30))
print(solution([1, 4, 4, 2], [6, 3, 8, 2], 59))
print(solution([1, 328, 467, 209, 54], [2, 7, 1, 4, 3], 1723))
print(solution([1, 99999, 100000, 99995], [9999, 9001, 9999, 9001], 3456789012))