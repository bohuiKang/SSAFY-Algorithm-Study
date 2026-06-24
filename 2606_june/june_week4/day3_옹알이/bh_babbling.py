def solution(babbling):
    # babbling의 각 문자열에서 "aya", "ye", "woo", "ma"는 각각 최대 한 번씩만 등장합니다.
    # 문자열 배열 babbling이 매개변수로 주어질 때, 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return.

    answer = 0
    words = ["aya", "ye", "woo", "ma"]

    for no in range(len(babbling)):
        word = babbling[no] # nephew가 발음할 수 있는지 확인할 단어
        check = 0   # 단어의 idx 번호
        right = True    # 발음할 수 있는 단어인지 확인

        while right and check < len(word):  # 아직 발음이 가능하고 idx번호가 초과되지 않으면 계속 확인

            match word[check]:  # switch 문
                case "a": 
                    if words[0] == word[check:check+3]:
                        check += 3
                    else:
                        right = False
                case "y":
                    if words[1] == word[check:check+2]:
                        check += 2
                    else:
                        right = False
                case "w":
                    if words[2] == word[check:check+3]:
                        check += 3
                    else:
                        right = False
                case "m":
                    if words[3] == word[check:check+2]:
                        check += 2
                    else:
                        right = False
                case _: # 기본값(Default)
                    right = False
        if right:   # 발음 가능한 단어임.
            answer += 1

    return answer

print(solution(["aya", "yee", "u", "maa", "wyeoo"]))
print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))

    ## match 문 (switch 문)

    # match status_code:
    # case 200:
    #     print("Success")
    # case 404:
    #     print("Not Found")
    # case 500 | 502:  # 여러 값 매칭 가능
    #     print("Server Error")
    # case _:           # 기본값 (Default)
    #     print("Unknown Status")

