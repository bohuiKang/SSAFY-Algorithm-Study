def solution(phone_book):
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        # 현재 번호의 길이 만큼 다음 번호의 앞부분과 비교
        if phone_book[i+1].startswith(phone_book[i]):
            return False

    return True
