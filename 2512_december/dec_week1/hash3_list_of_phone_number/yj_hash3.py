def solution(phone_book):
    phone_book.sort()  # 정렬해서 인접한 전화번호만 탐색하기
    for i in range(len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True

def solution(phone_book):
    phone_dict = {}
    for number in phone_book:
        phone_dict[number] = 1  # 해시맵에 전화번호 저장

    for number in phone_book:
        for i in range(1, len(number)):
            prefix = number[:i]
            if prefix in phone_dict:  # 접두사가 해시맵에 존재하는지 확인
                return False
    return True