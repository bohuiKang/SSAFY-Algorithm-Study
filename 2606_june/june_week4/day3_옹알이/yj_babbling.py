def solution(babbling):
    result = 0
    
    for b in babbling:
        visited = [False, False, False, False]  # aya, ye, woo, ma 사용 여부
        isResult = True  # 발음할 수 있는 단어인지 여부
        
        while len(b) > 0:  # b가 길이가 1 이상이어야 함
            # 맨 앞 글자가 a, y, w, m 중에서 있는지?
            if len(b) >= 3 and b[:3] == 'aya' and not visited[0]:
                visited[0] = True  # 'aya'가 사용되었다. 또 사용 못 함
                b = b[3:]  # 'aya'만큼 앞단어를 없애기
            elif len(b) >= 2 and b[:2] == 'ye' and not visited[1]:
                visited[1] = True
                b = b[2:]
            elif len(b) >= 3 and b[:3] == 'woo' and not visited[2]:
                visited[2] = True
                b = b[3:]
            elif len(b) >= 2 and b[:2] == 'ma' and not visited[3]:
                visited[3] = True
                b = b[2:]
            else: 
                isResult = False
                break  # 없으면 끝
        
        # 발음할 수 있으면 result += 1
        if isResult:
            result += 1

    return result