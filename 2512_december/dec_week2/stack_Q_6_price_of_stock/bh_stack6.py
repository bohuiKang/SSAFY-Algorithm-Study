def solution(prices):
    leng = len(prices)
    answer = [0] * leng
    for i in range(leng): # 0 ~ (leng-1)
        for j in range(i+1, leng): # i+1 을 함으로 마지막 요소는 for문을 작동하지 못한다. 
            answer[i] += 1
            if prices[i] > prices[j]: # 기준 값보다 다음 값이 작으면, pass
                break
    return answer

print(solution([1, 2, 3, 2, 3]))















# def solution(prices):
#     print(1)
#     answer = []
#     leng = len(prices)
#     for idx in range(leng): # 앞에서 출발
#         print(2)
#         for back in range(leng -1, idx, -1): # 뒤에서 idx로 출발
#             print(3)
#             if prices(idx) <= prices(back): # 비교 시점보다 끝의 값이 크거나 같으면,
#                 print(4)
#                 answer.append(back - idx)
#                 print(5)
#                 break
#     return answer

# print(solution([1, 2, 3, 2, 3]))