'''
시간 초과
def solution(phone_book):
    answer = True
    num = len(phone_book)
    for i in range(num):
        # 한개를 선택 후
        p = phone_book[i]
        n = len(p)
        # 나머지와 비교
        for j in range(num):
            # 비교값과 같은 번호면 건너뛰기
            if i == j:
                continue
            ph = phone_book[j]
            # 비교값의 자리수만큼 앞에서 떼어와서 비교
            if p == ph[:n]:
                answer = False
                break
        if answer == False:
            break

    return answer
'''

def solution(phone_book):
    answer = True
    num = len(phone_book)
    # 문자열 정렬, 사전순 정렬을 통해 비슷한것끼리 모이게 된다,
    phone_book = sorted(phone_book)
    for i in range(num):
        # 한개를 선택 후
        p = phone_book[i]
        n = len(p)
        # 다음 것과 비교, 그전에 i+1이 num이 된다면 순회가 끝난것이므로 종료
        if i + 1 == num:
            break
        ph = phone_book[i + 1]
        # 비교값의 자리수만큼 앞에서 떼어와서 비교
        if p == ph[:n]:
            # 같다면 접두사가 있으므로 answer 갱신, 반복문 종료
            answer = False
            break

    return answer