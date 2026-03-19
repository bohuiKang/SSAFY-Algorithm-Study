# 이분탐색
def solution(diffs, times, limit):
    # diff 현재 퍼즐의 난이도
    # time_cur 현재 퍼즐의 소요 시간
    # time_prev 이전 퍼즐의 소요 시간
    # level 숙련도

    answer = 0  # 답 구해졌나?
    n = len(diffs)  # n 퍼즐의 개수
    # level 이분탐색
    left = 1
    right = max(diffs)  # 최대 난이도만큼 레벨이면 무조건 통과

    while left < right:
        mid_level = (left + right) // 2
        time = 0  # 현재 레벨로 퍼즐을 다 푸는 데 걸리는 시간

        # 퍼즐 다 풀기
        for i in range(n):  # 퍼즐 하나 풀기 * n번

            diff = diffs[i]  # diff 현재 퍼즐의 난이도
            time_cur = times[i]  # time_cur 현재 퍼즐의 소요 시간
            # 이전 퍼즐이 있다면 time_prev도 생성

            if diff <= mid_level:  # diff ≤ level이면 퍼즐을 틀리지 않고 time_cur만큼의 시간을 사용하여 해결합니다.
                time += time_cur
            elif diff > mid_level:  # diff > level이면, 퍼즐을 총 diff - level번 틀립니다.
                if i > 0:
                    time_prev = times[i - 1]  # time_prev 이전 퍼즐의 소요 시간
                    time += (time_cur + time_prev) * (diff - mid_level) + time_cur
                else:
                    time += time_cur * (diff - mid_level) + time_cur

        # time이 limit을 넘기지 않았으면 answer 갱신하고 레벨 범위 높이기
        if time <= limit:  # 레벨이 너무 높음
            right = mid_level
        else:  # 레벨이 너무 낮음
            left = mid_level + 1


    return right


# 답은 3, 2, 294, 39354
# print('#1', solution([1, 5, 3], [2, 4, 7], 30))
# print('#2', solution([1, 4, 4, 2], [6, 3, 8, 2], 59))
# print('#3', solution([1, 328, 467, 209, 54], [2, 7, 1, 4, 3], 1723))
# print('#4', solution([1, 99999, 100000, 99995], [9999, 9001, 9999, 9001], 3456789012))