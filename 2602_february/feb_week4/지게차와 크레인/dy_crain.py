from collections import deque


def solution(storage, requests):
    n = len(storage)
    m = len(storage[0])

    # 테두리를 '0'으로 감싸는 패딩 생성
    # 외부와 연결된 빈 공간을 '0'으로 표시합니다.
    padded_storage = [['0'] * (m + 2)]
    for row in storage:
        padded_storage.append(['0'] + list(row) + ['0'])
    padded_storage.append(['0'] * (m + 2))

    # 지게차 작동 (외부와 연결된 타겟 제거)
    def fork_lift(target):
        # 이번 턴에 지워질 좌표들을 저장 (동시 제거를 위함)
        to_remove = []
        visited = [[False] * (m + 2) for _ in range(n + 2)]
        q = deque([(0, 0)])
        visited[0][0] = True

        while q:
            r, c = q.popleft()
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n + 2 and 0 <= nc < m + 2 and not visited[nr][nc]:
                    # 빈 공간이면 계속 이동
                    if padded_storage[nr][nc] == '0':
                        visited[nr][nc] = True
                        q.append((nr, nc))
                    # 타겟 컨테이너를 만나면 제거 목록에 추가 (이동은 중단)
                    elif padded_storage[nr][nc] == target:
                        visited[nr][nc] = True
                        to_remove.append((nr, nc))

        for r, c in to_remove:
            padded_storage[r][c] = '0'
        return len(to_remove)

    # 크레인 작동 (위치 상관없이 모두 제거)
    def crane(target):
        count = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if padded_storage[i][j] == target:
                    padded_storage[i][j] = '0'
                    count += 1
        return count

    # 출고 요청 처리
    total_removed = 0
    for re in requests:
        if len(re) == 1:
            total_removed += fork_lift(re)
        else:
            # "AA" -> "A"만 추출
            total_removed += crane(re[0])

    return (n * m) - total_removed