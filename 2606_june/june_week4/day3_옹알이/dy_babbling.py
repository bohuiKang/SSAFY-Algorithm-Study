def solution(babbling):
    answer = 0
    nephew = ["aya", "ye", "woo", "ma"]
    for word in babbling:
        # 각 발음은 한번씩만 할 수 있으니까 발음 가능한 문자의 최대 길이 10
        if len(word) > 10:
            continue
        for nep in nephew:
            # replace(대체될 단어, 대체할 단어, 횟수), 재할당 필수
            # 공백으로 대체할시 서로 다른 단어가 결합되기에 " "로 치환
            word = word.replace(nep, " ", 1)
        # 넣었던 띄어쓰기 제거
        word = word.strip(" ")
        # word가 비었다면 발음 가능한 단어
        if not word:
            answer += 1
        
    return answer

print(solution(["aya", "yee", "u", "maa", "wyeoo"]))