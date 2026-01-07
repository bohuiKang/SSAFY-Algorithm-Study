def solution(array, commands):
    answer = []
    for i, j, k in commands:
        # 자르기
        sliced_array = array[i-1:j]
        # 정렬하기
        sliced_array.sort()
        # k번째 숫자
        num = sliced_array[k-1]
        # answer에 추가
        answer.append(num)
    return answer