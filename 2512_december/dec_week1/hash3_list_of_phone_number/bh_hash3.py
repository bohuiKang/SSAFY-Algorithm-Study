# 같은 전화번호가 중복해서 들어있지 않습니다.
def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if len(phone_book[i]) < len(phone_book[i+1]): # 앞번호가 뒷번호보다 길이 작고(같으면 애초에 다른 값)
            if phone_book[i] == phone_book[i+1][:len(phone_book[i])]: # 앞번호의 길이만큼 뒷번호의 길이를 잘랐을때 같다면 false
                answer = False
                break
    
    return answer