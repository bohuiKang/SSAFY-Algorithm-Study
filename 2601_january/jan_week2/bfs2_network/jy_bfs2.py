from collections import deque


def solution(n, computers):
    visited = [False] * n
    count = 0  # 네트워크 개수

    # 1번 컴퓨터부터 n번 컴퓨터
    for i in range(n):

        # 체크가 되지 않은 컴퓨터일 경우
        if visited[i] == False:
            count += 1  # 네트워크 추가

            q = deque([i])  # 할 일 목록(큐)에 시작점 등록
            visited[i] = True  # 방문 체크

            # 할 일 목록이 빌 때까지(연결된 애들 다 찾을 때까지) 반복
            while q:
                current = q.popleft()  #

                # current 컴퓨터랑 연결된 다른 컴퓨터들
                for neighbor in range(n):
                    # 연결되어 있고(1), 아직 안 가본 곳일 경우
                    if computers[current][neighbor] == 1 and not visited[neighbor]:
                        visited[neighbor] = True  # 방문 체크
                        q.append(neighbor)  # 큐에 추가

    return count