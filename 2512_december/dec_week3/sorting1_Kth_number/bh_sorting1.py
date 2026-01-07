def solution(array, commands):
    answer = []
    array = [0] + array
    print(array)
    for com in commands:
        i, j, k = com
        temp_arr = array[i:j+1]
        temp_arr.sort()
        answer.append(temp_arr[k-1])

    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))