nums = [3,1,2,3]

def solution(nums):
    answer = 0
    cnt = len(nums) // 2 # 고를수 있는 폰켓몬 수 (폰 이었잖아?)
    phone_dic ={}
    for num in nums: # 포켓몬 종류별로 dic 만들기
        if num in phone_dic:
            phone_dic[num] += 1
        else:
            phone_dic[num] = 1
            
    max_phone_num = len(phone_dic) # 폰켓몬 종류 개수
    if cnt <= max_phone_num:
        answer = cnt
    else:
        answer = max_phone_num 
    return answer
print(solution(nums))