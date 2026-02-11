def solution(n, costs):
    # 각 다리 비용을 기준으로 오름차순 정렬
    costs.sort(key= lambda x:x[2])
    # 부모들 자리를 만들어둚
    parents = [i for i in range(n)]

    # 부모 찾기
    def find_set(x):
        # 만약 자신이 부모일 경우 함수 중단
        if x == parents[x]:
            return x
        # 아닐 경우 계속해서 반복 + 함축
        parents[x] = find_set(parents[x])
        return parents[x]

    # 사이클 합치기
    def union(x, y):
        rx = find_set(x)
        ry = find_set(y)
        # 사이클이 같지 않을 경우
        if rx != ry:
            if rx < ry:
                parents[ry] = rx
            else:
                parents[rx] = ry
            return True # 사이클 연결 성공 시 True 반환
        return False # 이미 연결되어 있었을 경우 Pass

    cnt = 0
    cost = 0

    for s, e, c in costs:
        # 사이클 연결되지 않았을 경우 연결
        if union(s, e):
            # 그만큼 카운트와 비용 증가
            cnt += 1
            cost += c
            # cnt == 간선개수가 n-1 개가 되면 끝난거
            if cnt == n - 1:
                break

    return cost