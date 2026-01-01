def solution(numbers):
    answer = ''
    for i in range(len(numbers)): # 정수의 맨 앞자리 기준으로 정렬하기 위해 2자리 이상의 정수 리스트로 만들어 자리수 분리
        num = numbers[i]
        if num >= 10:
            numbers[i] = list(map(int, str(num)))
        else: # 1자리 정수는 바로 리스트에 넣음 (정수, 리스트 섞여있으면 타입이 달라 정렬 불가능)
            numbers[i] = [num]

    numbers.sort(reverse = True) # 리스트 0 인덱스 기준으로 정렬


    # 잘못됨 이렇게 되면 다시 확인을 해줘야함
    # for i in range(len(numbers)-1, 0, -1): # 그런데 [3], [3,0]의 경우 3이 뒤에 가버리는 문제가 있어서 이를 해결위함
    #     num1 = numbers[i-1]
    #     num2 = numbers[i]
    #     if len(num1) <= len(num2):
    #         continue

    #     if num1[0:len(num2)] == num2 and num1[len(num2)] < num2[-1]: # 뒤쪽의 수가 앞쪽 수에 포함 관계에 있는 경우만 처리
    #         numbers[i-1], numbers[i] = numbers[i], numbers[i-1]


# key = lambda x: (-x[0], len(x))
    for num in numbers:
        answer += "".join(map(str,num))
    return answer


print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))