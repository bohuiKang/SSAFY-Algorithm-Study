def solution(array, commands):
    
    tc = len(commands)
    answer = [0]*tc

    for i in range(tc):
        first = commands[i][0] - 1
        last = commands[i][1]
        k = commands[i][2] - 1

        new_arr = sorted(array[first:last])
        answer[i] = new_arr[k]
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))