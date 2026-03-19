# re 가 1개면 지게차, 2개면 크레인

from collections import deque

# 컨테이너 출고 요청 및 최종 관리
def solution(storage, requests):
    row = len(storage)          # 행의 개수
    column = len(storage[0])    # 열의 개수
    answer = row * column       # 컨테이너 개수
    storage = [list(cons) for cons in storage]
    new_storage = [['e'] * (column + 2) for _ in range(row + 2)]

    # 빈공간 테두리 만들기
    for r in range(row):
        for c in range(column):
            new_storage[r+1][c+1] = storage[r][c]

    # 1. requests 하나씩 for문
    for idx in range(len(requests)):
        # 2. 요청 값의 길이 확인
        if len(requests[idx]) == 1: # 2-1. 하나면, 지게차 True
            # 3. 컨테이너 출고 요청 => row, column, storage, requests 요청 하나, 지게차(True) or 크레인(False)
            answer -= release(row+2, column+2, new_storage, requests[idx], True)        # 출고된 값 빼기
        else: # 2-2. 두개면, 크레인 False
            answer -= release(row+2, column+2, new_storage, requests[idx][0], False)    # 2개 중 한 개만 전달 

    return answer

# 컨테이너 출고 진행
def release(row, column, new_storage, request, is_forklift):
    container = 0 # 출고되는 컨테이너 개수 저장할 변수
    targets = []
    visited = [[False] * column for _ in range(row)]

    # bfs
    q = deque([(0, 0)])
    visited[0][0] = True

    while q:
        r, c = q.popleft()

        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr = r+dr
            nc = c+dc
            if new_storage[nr][nc] == 'e' and not visited[nr][nc]:
                visited[nr][nc] = True
                q.append((nr, nc))

    # storage를 순회
    for r in range(1, row -1):
        for c in range(1, column -1):
            if new_storage[r][c] == request:
                # 1. 지게차일 때,
                if is_forklift:
                    # 주변(상하좌우)에 하나라도 visited가 True인 곳이 있는지 확인
                    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                        if visited[r+dr][c+dc]:
                            targets.append((r, c))
                            container += 1          # container 추가
                            break

                # 2. 크레인일 때,
                else: 
                    # 2-1. 해당되는 컨테이너 위치 상관없이 소문자e로 변경, container 추가
                    targets.append((r, c))
                    container += 1
    for r, c in targets:
        new_storage[r][c] = 'e' # 해당 위치 값을 소문자e로 변경

    return container # 출고된 컨테이너 수 반환 


print(solution(["AZWQY", "CAABX", "BBDDA", "ACACA"], ["A", "BB", "A"]))
# print(solution(["HAH", "HBH", "HHH", "HAH", "HBH"], ["C", "B", "B", "B", "B", "H"]))