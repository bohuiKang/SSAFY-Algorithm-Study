from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def solution(storage, requests):
    # storage의 가로 m, 세로 n 구하기
    n = len(storage)
    m = len(storage[0])

    # '0'으로 둘러싸기 - dfs 할 공간 있어야 하니까.
    board = [['0'] * (m + 2) for _ in range(n + 2)]
    # 다시 가운데에 storage 넣기
    for x in range(n):
        for y in range(m):
            board[1+x][1+y] = storage[x][y]

    N = n + 2
    M = m + 2


    # bfs 돌리기 - 없앤건 숫자 0으로 바꾸기
    def BFS():
        # 초기화
        visited = [[False] * M for _ in range(N)]
        Q = deque([(0, 0)])  # 탐색할 좌표 (x, y)
        visited[0][0] = True

        outer = set()  # 외부 공기와 직접 맞닿은 좌표 모음, 한 컨테이너가 양방향에서 공기 맞을 수 있으니 set으로 걸러야함

        # BFS 돌리기
        while Q:
            curX, curY = Q.popleft()  # 큐에서 탐색할거 꺼내기
            for dir in range(4):
                nx = curX + dx[dir]
                ny = curY + dy[dir]
                if nx < 0 or nx >= N or ny < 0 or ny >= M: continue  # 범위 밖이면 continue
                if visited[nx][ny]: continue  # 이미 방문했으면 continue
                # 공기면 계속 퍼짐
                if board[nx][ny] == '0':
                    visited[nx][ny] = True
                    Q.append((nx, ny))
                else:
                    # 외부 공기와 닿은 컨테이너
                    outer.add((nx, ny))
        return outer

    # 요청 처리
    for req in requests:

        outer = BFS()

        # 길이 2 - 크레인 - 모두 찾기
        if len(req) == 2:
            target = req[0]
            for i in range(N):
                for j in range(M):
                    if board[i][j] == target:
                        board[i][j] = '0'

        # 길이 1 - 지게차 - 겉에만 찾기
        else:
            target = req

            for x, y in outer:
                if board[x][y] == target:
                    board[x][y] = '0'

    # 남은 컨테이너 수 세기
    answer = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if board[i][j] != '0':
                answer += 1

    return answer  # 남은 컨테이너 수 return


# 답은 11, 4
print(solution(["AZWQY", "CAABX", "BBDDA", "ACACA"], ["A", "BB", "A"]))
print(solution(["HAH", "HBH", "HHH", "HAH", "HBH"], ["C", "B", "B", "B", "B", "H"]))