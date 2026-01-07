import heapq

def solution(operations):
    # 최소힙
    min_heap = [] 
    # 최대힙 (음수로 저장, 힙은 작은 값을 우선으로 처리하기에) 
    max_heap = []  
    
    # 명령어 하나씩 처리
    for op in operations:
        cmd, num = op.split()
        num = int(num)
        
        if cmd == 'I':
            # 양쪽 힙에 모두 추가
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
        
        # 힙이 비어있지 않을 때만
        elif cmd == 'D' and min_heap:  
            if num == 1:
                # 최댓값 삭제, 최대힙에서 pop
                heapq.heappop(max_heap)
                # 최소힙 동기화
                min_heap = [-x for x in max_heap]
                heapq.heapify(min_heap)
            else:
                # 최솟값 삭제, 최소힙에서 pop
                heapq.heappop(min_heap)
                # 최대힙 동기화
                max_heap = [-x for x in min_heap]
                heapq.heapify(max_heap)
    
    # 결과 반환
    if min_heap:
        return [-max_heap[0], min_heap[0]]
    return [0, 0]