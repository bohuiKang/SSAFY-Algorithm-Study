from collections import deque

def solution(priorities, location):
    # (우선순위, 원래위치) 형태로 큐 생성
    q = deque()
    for i in range(len(priorities)):
        q.append((priorities[i], i))

    # 몇 번째로 실행되는지 카운트
    order = 0  
    
    while q:
        # 큐의 맨 앞 프로세스
        current = q.popleft()  # (우선순위, 인덱스)
        
        # 남은 큐에 현재보다 높은 우선순위 있나 확인
        # any(): 조건 만족하는 게 하나라도 있으면 True
        if any(current[0] < qu[0] for qu in q):
            # 더 높은 우선순위가 있으면 맨 뒤로 보내기
            q.append(current)
        else:
            # 가장 높은 우선순위면 실행
            order += 1
            
            # 목표 프로세스인지 확인
            if current[1] == location:
                return order