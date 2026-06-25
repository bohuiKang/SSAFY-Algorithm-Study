def solution(babbling):
    words = ["aya", "ye", "woo", "ma"]
    answer = 0

    for bab in babbling:
        for word in words:
            # 단어를 words 내의 word로 치환할 수 있으면 공백으로 처리
            # 아예 없애면 테케 1번에서 wyeoo -> ye 제거 -> woo 가 되어 통과되어버림
            # 그래서 공백을 둬야함
            bab = bab.replace(word, " ")
            # bab이 다 비면 발음 다 가능
        if bab.strip() == "":     
            answer += 1

    return answer