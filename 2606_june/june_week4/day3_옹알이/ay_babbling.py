def solution(babbling):
    answer = 0
    can_talk = ["aya", "ye", "woo", "ma"]
    for word in babbling: # babbling 배열에서 문자열 하나씩 꺼내오기
        for can in can_talk: # 발음 가능한 단어 하나씩 꺼내서 문자열에 포함되어 있는지 확인
            if can not in word: # 없으면 건너뛰기
                continue

            word = word.replace(can, " ") # 있으면 발음 가능한 문자열 띄워쓰기로 대체

        if not word.strip(): # 공백 제거하면 false기 때문에 빈값이면 해당 문자열로 표기 가능이라서
            answer += 1

    return answer

print(solution(["aya", "yee", "u", "maa", "wyeoo"]))
print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))