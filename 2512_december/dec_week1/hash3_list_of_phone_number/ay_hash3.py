phone_book = ["123","456","789"]

def solution(phone_book):
    answer = True
    phone_book.sort()
    # 정렬하면 접두사 포함될경우 무조건 옆에 위치하게 됨
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][0:len(phone_book[i])]:
            answer = False
            return answer
    return answer


# 처음에 잘 못 생각함 제알 짧은 것만 선택해서 고르면 된다고 생각해 버림

# def solution(phone_book):
#     answer = True
#     phone_cnt = len(phone_book)
#     min_len = float("inf")
#     idx = [0]
#     # 제일 짧은 길이만 접두사 될 수 있으니까 찾기
#     for i in range(phone_cnt):
#         if min_len > len(phone_book[i]):
#             min_len = len(phone_book[i])
#             idx = [i]
#         elif min_len == len(phone_book[i]):
#             idx += [i]

#     while idx:
#         first_num_idx = idx.pop()
#         first_num = phone_book[first_num_idx]
#         for i in range(phone_cnt):
#             if  first_num_idx == i: # 같은건 검사하지 말고 건너뛰
#                 continue
#             if first_num == phone_book[i][0:min_len]:
#                 answer = False
#                 return answer

#     return answer

print(solution(phone_book))