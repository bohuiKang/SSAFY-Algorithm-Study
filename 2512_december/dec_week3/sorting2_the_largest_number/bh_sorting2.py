from functools import cmp_to_key

def solution(numbers):
    answer = ''

    str_arr = [str(num) for num in numbers]

    def compare(x, y): # x가 앞에 오려면 음수, y가 앞에 오려면 양수 리턴
        if x + y > y + x:
            return -1
        elif y + x > x + y:
            return 1
        return 0 # x와 y가 같음
    
    str_arr.sort(key=cmp_to_key(compare))

    if str_arr[0] == '0': # 원소가 전부 0일 때,
        answer = '0'
    else:
        answer = ''.join(str_arr)
    return answer

print(solution([3, 30, 34, 5, 9]))



''' 시간초과 '''
# def solution(numbers):
#     answer = ''

#     str_arr = [str(num) for num in numbers]
#     for i in range(len(str_arr)):
#         for j in range(i, len(str_arr)):
#             if str_arr[i] + str_arr[j] < str_arr[j] + str_arr[i]:
#                 temp = str_arr[i]
#                 str_arr[i] = str_arr[j]
#                 str_arr[j] = temp

#     if str_arr[0] == 0:
#         answer = '0'
#     else:
#         answer = ''.join(str_arr)
#     return answer

# print(solution([3, 30, 34, 5, 9]))