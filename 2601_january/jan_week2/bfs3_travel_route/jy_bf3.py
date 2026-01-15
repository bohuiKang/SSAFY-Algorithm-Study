def solution(tickets):
    answer = []
    # 쓴 티켓 확인
    visited = [False] * len(tickets)

    # 티켓 정렬 (알파벳 순서)
    tickets.sort()

    # current: 현재 위치 공항
    # path: 지금까지 방문한 공항들의 경로
    # count: 사용한 티켓의 개수
    def dfs(current, path, count):
        # 종료조건: 사용한 티켓 개수가 본래 티켓 길이와 같을 경우 -> 티켓 다 씀
        if count == len(tickets):
            answer.append(path)
            return True

        # 카드를 사용하지 않았고 카드 출발지가 current와 같다면
        for i in range(len(tickets)):
            if not visited[i] and tickets[i][0] == current:
                # 카드 씀
                visited[i] = True
                # 재귀를 통해 도착지를 계속 찾아나감
                if dfs(tickets[i][1], path + [tickets[i][1]], count + 1):
                    return True

                # 백트래킹
                visited[i] = False

        # 경로를 못찾았으면 False -> 경로 불가능. 다른 거 찾기
        return False

    # 출발지는 무조건 ICN이니까 미리 넣어두고 시작
    dfs("ICN", ["ICN"], 0)

    return answer[0]