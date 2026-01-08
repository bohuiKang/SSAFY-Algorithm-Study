from collections import defaultdict, deque

def solution(n, wires):
    # 연결되어있는 송전탑의 수 세기
    def count_connect(node):
        # 송전탑(노드)의 수
        cnt = 0
        # 방문 기록
        visited = [True]*(n+1)
        # 방문 목록
        q = deque()

        #방문 목록에 해당 노드 추가, 방문 기록에도 추가
        q.append(node)
        visited[node] = False

        while q:
            # 현재 노드
            now = q.pop()
            # 노드의 수 증가
            cnt += 1
            # 연결되어있는 노드 탐색
            for next in lst[now]:
                # 방문한적 없다면
                if visited[next]:
                    # 방문 목록, 기록에 추가
                    q.append(next)
                    visited[next] = False
        return cnt
    
    # 최소 차이값을 저장할 변수
    answer = float('inf')
    # 연결 그래프
    lst = defaultdict(list)

    # 트리 구현
    for w1, w2 in wires:
        lst[w1].append(w2)
        lst[w2].append(w1)

    # 전선 하나씩 끊어보기
    for w1, w2 in wires:
        lst[w1].remove(w2)
        lst[w2].remove(w1)

        # 한쪽 네트워크의 송전탑 개수를 센 후, 두 네트워크의 차이 계산
        num  = abs(n - count_connect(w1)*2)

        # 최소값 갱신
        if answer > num:
            answer = num

        # 연결 초기화
        lst[w1].append(w2)
        lst[w2].append(w1)        


    return answer

print(solution(4, [[1,2],[2,3],[3,4]]))