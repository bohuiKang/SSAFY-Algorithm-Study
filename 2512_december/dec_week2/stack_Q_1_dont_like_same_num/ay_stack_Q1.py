
arr = [1,1,3,3,0,1,1]

def solution(arr):
    answer = []
    for num in arr:
        if not answer: # 비어있으면 건너뛰기
            answer.append(num)
            continue
        if answer[-1] == num:
            continue
        
        answer.append(num)
        

        
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    return answer

print(solution(arr))
