def solution(clothes):
    answer = 0
    
    answer = check(0, [], clothes, 0)
    
    return answer

def check(point, clothe_type, clothes, cnt):
    
    if point == len(clothes)-1:
        return cnt
    
    for i in range(point, len(clothes)):
        if clothes[i][1] not in clothe_type:
            check(point + 1, clothe_type + [clothes[i][1]], clothes, cnt + 1)
        else:
            check(point + 1, clothe_type, clothes, cnt)
        
ans = solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])

print(ans)


