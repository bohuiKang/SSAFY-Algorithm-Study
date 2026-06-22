def solution(diffs, times, limit):
    # 1. 특정 숙련도(level)일 때 총 소요 시간을 계산하는 함수
    def get_total_time(level):
        total = 0
        for i in range(len(diffs)):
            diff = diffs[i]
            cur_t = times[i]
            prev_t = times[i - 1] if i > 0 else 0

            if diff <= level:
                total += cur_t
            else:
                # 틀리는 횟수: diff - level
                # 한 번 틀릴 때마다 (cur_t + prev_t) 추가 소요
                # 마지막에 성공할 때 cur_t 추가 소요
                error_count = diff - level
                total += error_count * (cur_t + prev_t) + cur_t

            # 계산 도중 이미 limit을 넘어서면 조기 종료 (최적화)
            if total > limit:
                return total
        return total

    # 2. 이진 탐색 범위 설정
    # 숙련도의 최소값은 1, 최대값은 난이도 중 최대값으로 설정
    low = 1
    high = max(diffs)
    answer = high

    while low <= high:
        mid = (low + high) // 2

        # 3. 현재 숙련도로 limit 내에 해결 가능한지 확인
        if get_total_time(mid) <= limit:
            # 성공했다면, 더 낮은 숙련도가 있는지 확인하기 위해 범위를 좁힘
            answer = mid
            high = mid - 1
        else:
            # 실패했다면, 숙련도를 높여야 함
            low = mid + 1

    return answer