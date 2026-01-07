import heapq

def solution(operations):
    heap = []
    
    for op in operations:
        command, value = op.split()
        num = int(value)
        
        if command == 'I':
            # 데이터를 넣을 때는 최소 힙 형태 유지
            heapq.heappush(heap, num)
        
        elif command == 'D':
            if not heap:  # 큐가 비어있으면 무시
                continue
                
            if num == 1:
                # 최댓값 삭제
                heap.remove(max(heap))
                heapq.heapify(heap)  # 다시 힙으로 만들기
            else:
                # 최솟값 삭제
                heapq.heappop(heap)
                
    # 연산 다 돌린 후
    if not heap:  # 큐가 비어있으면
        return [0, 0]
    else:  # [최대, 최소] 반환
        return [max(heap), min(heap)]
        