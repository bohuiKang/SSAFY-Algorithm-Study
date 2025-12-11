from collections import deque, defaultdict

# 1. max 값 계속 구하기 => 시간초과
# 2. dict로 우선순위 개수 체크하기 => 시간초과
# 3. 정렬로 한칸씩 옮겨서 max 값 찾기 => ok

def solution(priorities, location):
    q = deque()
    max_prior = max(priorities) # max 우선순위
    # prior_how_many = defaultdict(int) # 우선순위별 작업 개수 => 시간초과
    sort_prior = sorted(priorities, reverse=True)
    
    for i in range(len(priorities)):
        q.append((i, priorities[i])) # (위치번호, 우선순위)
        # prior_how_many[priorities[i]] += 1
    
    answer = 0 # 실행 순서 저장 변수
    while q:
        no, prior = q.popleft()
        if prior == max_prior: # 우선순위가 같을 때,
            answer += 1
            # prior_how_many[prior] -= 1 # 개수 차감
            if no == location: # 알고 싶은 순서와 위치번호가 같을 때, 
                return answer
            max_prior = sort_prior[answer]
            # if prior_how_many[prior] == 0: # 개수가 0일 때,
                # max_prior = max(prior_how_many)
                # max(q, key=lambda x: x[1]) # max 우선순위 다시 구하기 => 시간초과
        else: # 우선순위가 낮을 때,
            q.append((no, prior))

    return answer