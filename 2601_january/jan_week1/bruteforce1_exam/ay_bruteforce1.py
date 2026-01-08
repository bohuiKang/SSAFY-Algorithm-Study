def cal_score(arr, answers): # 점수 계산하는 함수
    re_num = len(arr) # 반복되는 길이 구하기
    i = 0
    score = 0 
    for answer in answers: 
        if arr[i] == answer:
            score += 1
        i = (i+1) % re_num # 반복값 적용위해 반복되는 길이로 나눈 나머지로 i 값 넣어줌
    
    return score


def solution(answers):
    answer = []
    first = [ 1, 2, 3, 4, 5 ] # 반복 5개
    second = [ 2, 1, 2, 3, 2, 4, 2, 5 ] # 반복 8개
    third = [ 3, 3, 1, 1, 2, 2, 4, 4, 5, 5 ] # 반복 10개

    # 해당 수포자에 대한 점수값 딕셔너리
    dic = {
        1: cal_score(first, answers),
        2: cal_score(second, answers),
        3: cal_score(third, answers),
    }
    max_val = max(dic.values()) # 딕셔너리 값에대한 최대값 구하기

    for key, value in dic.items(): # max 값과 같은 value 값 가지면 answer 리스트에 append
        if value == max_val:
            answer.append(key)
    answer.sort()
    return answer

print(solution([1,2,3,4,5]))