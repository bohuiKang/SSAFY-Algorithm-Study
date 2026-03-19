def solution(n, w, num):
    answer = 0
    # 마지막 층 몫과 나머지 구하기
    left_last = n % w
    level_last = n // w

    if left_last: # 나머지가 있으면 몫 + 1층이 최고층
        level_last += 1


    # 최고층 시작 혹은 끝점 인덱스 구하기 (기준 인덱스 구하기)
    # 홀수층이면 왼쪽에서 오른쪽 쌓기 , 짝수면 반대
    if not level_last % 2: # 짝수층
        check_last_even = 0
        if left_last == 0:
            high_idx = 0
        else:
            high_idx = w - left_last # 최고층 시작 인덱스
    else: # 홀수층
        check_last_even = 1
        if left_last == 0:
            high_idx = w - 1
        else:
            high_idx = left_last - 1 # 최고층 마지막 인덱스

    # 꺼내야 하는 번호
    left_num = num % w
    level_num = num // w

    if left_num: # 나머지가 있으면 몫 + 1층이 현재 층
        level_num += 1

    # 현재층 인덱스 구하기
    if not level_num % 2: #짝수층이면 오른쪽에서 왼쪽
        if left_num == 0:
            num_idx = 0
        else:
            num_idx = w - left_num
    else: # 홀수층이면 왼쪽에서 오른쪽
        if left_num == 0:
            num_idx = w - 1
        else:
            num_idx = left_num - 1

    # 최고층 인덱스와 비교하기
    if not check_last_even: # 짝수층
        if high_idx <= num_idx:
            answer = level_last - level_num + 1
        else:
            answer = level_last - level_num
    else:
        if high_idx >= num_idx:
            answer = level_last - level_num + 1
        else:
            answer = level_last - level_num


    return answer


print(solution(22, 6, 8))
print(solution(13, 3, 6))
'''
n // w 와 n % w 값을 이용하자
13 // 3 -> 4 *3 + 1 -> 5층 이라는 뜻
13 % 3 -> 1 나머지 있음 -> 몫 + 1 층 이 최고층
12 // 3 -> 4 나머지 없음 몫이 최고층


1층 왼쪽이 작은 수
2층 오른쪽이 작은 수
3층 왼쪽이 작은 수
4층 오른쪽이 작은 수 

정할것 현재층을 표시할 것인지


6 // 3 2 층 -> 꺼내야 하는 번호 층수 구하고 인덱스 번호 위치 구하기
6 //3 -> 2층 오른쪽 부터 6 % 3 == 0 2층 0이면 1층 
5 //3 -> 1 5 % 3 == 2 인덱스 번호 w-2 위치 3 -2 = 1번 인덱스 2층
최고층 인덱스 번호 랑 비교해서 
최고층 홀수면  -> 최고층 인덱스 번호 보다 이하면 -> 최고층 - 현재층 + 1 / 초과면 최고층 - 현재층
최고층 짝수면 -> 최고층 인덱스 번호보다 이상이면 -> 최고층 - 현재층 +1 / 미만이면 최고층 - 현재층

최고층이 홀 수 면 왼쪽 부터 최고층이 인덱스 번호 까지
나머지가 1이면 -> 1-1 0번 까지

짝수면 0~(w-1-나머지) 까지: 최고층 -1  w-나머지 ~ w - 1 번 까지  최고층
층마다 
'''