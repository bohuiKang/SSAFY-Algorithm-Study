def solution(arr):
    answer = [arr[0]]  # 첫 번째 원소를 넣고 초기화
    # 이전 원소와 같으면 pass, 다르면 넣기
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]: pass
        else: answer.append(arr[i])
    return answer