from collections import deque

# 송전탑 개수 세기
def count(start, n, graph):
    visited = [False] * (n + 1)
    queue = deque([start])
    visited[start] = True
    cnt = 1

    # 나의 사랑 큐를 돌림
    while queue:
        current = queue.popleft()
        # 만약 해당 탑과 연결되어 있는 다른 탑이
        for nxt in graph[current]:
            # 방문하지 않았을 경우 -> True로 바꾼 뒤 queue에 다음에 갈 곳으로 추가, cnt + 1
            if visited[nxt] == False:
                visited[nxt] = True
                queue.append(nxt)
                cnt += 1

    return cnt

def solution(n, wires):
    # n은 송전탑의 개수, wires는 전선 정보

    # 해답은 일단 제일 최댓값으로 해놓음
    answer = n + 1
    graph = [[] for _ in range(n + 1)]
    # 그래프에 값을 배당
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)

    # 전선을 하나씩 다 끊음
    for v1, v2 in wires:
        graph[v1].remove(v2)
        graph[v2].remove(v1)

        # 전선을 끊은 뒤 양 쪽 개수 세기
        cnt_1 = count(v1, n, graph)
        cnt_2 = n - cnt_1

        # 차이 계산 후 현재 answer보다 작다면 갱신
        diff = abs(cnt_2 - cnt_1)
        if diff < answer:
            answer = diff

        # 끊은 전선을 복구
        graph[v1].append(v2)
        graph[v2].append(v1)

    return answer

# ----------------
# 개인 코드 공부
def solution(n, wires):

    ans = n
    # 전선 하나를 끊는 부분
    # 리스트 슬라이싱으로 wires[:i]는 0번부터 i-1까지, wires[i+1:]는 i+1번부터 끝까지 전선이니
    # 둘을 더하면 i번째 전선만 뺀 리스트를 볼 수 있음
    for sub in (wires[i+1:] + wires[:i] for i in range(len(wires))):
        # sub가 i번째 전선이 빠지고 남은 전선들
        # s는 첫 번째 전선을 set에 넣은 것 -> 1번 전력망의 발화점
        s = set(sub[0])
        # 뭐야 이게? 미친 아마 BFS를 대체하는 부분같음
        # 전선 개수만큼 반복하며(for _ in sub) 전선을 꺼내봄(for v in sub)
        # 만약 전선 하나(set(v))가 현재 전력망 덩어리(s)와 연결되어 있다면(& -> 교집합)
        # 전선에 포함된 송전탑 번호를 s에 추가해 전력망을 확장
        [s.update(v) for _ in sub for v in sub if set(v) & s]
        # 최솟값 갱신
        ans = min(ans, abs(2 * len(s) - n))

    return ans