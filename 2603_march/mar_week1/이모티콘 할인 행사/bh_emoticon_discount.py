# 카카오톡 사용자 n명의 구매 기준을 담은 2차원 정수 배열 users [비율, 가격]
# 이모티콘 m개의 정가를 담은 1차원 정수 배열 emoticons

def solution(users, emoticons):
    answer = [] # 가입자수, 판매액
    discount = [10, 20, 30, 40] # 할인율
    dis_set = []

    # 할인율 조합
    def make_dis_set(dis_lst):

        if len(dis_lst) == len(emoticons):
            dis_set.append(dis_lst)
            return 
        
        for dis in discount:
            make_dis_set(dis_lst + [dis])

    # 이모티콘 할인률 조합
    make_dis_set([])
    # print(dis_set)
    max_plus = 0
    max_sale = 0
    for diss in dis_set:
        total_plus = 0 # 플러스 서비스 가입자
        total_sale = 0 # 판매액 합계
        for stand_rate, stand_price in users:
            amount = 0 # 구매 금액
            for i in range(len(emoticons)):
                if diss[i] >= stand_rate: # 기준 할인율 보다 할인이 크면
                    amount += emoticons[i] * (1 - diss[i]/100)
            if amount >= stand_price: # 기준 금액보다 총 금액이 크다면
                total_plus += 1
            else: # 기준 금액보다 총금 액이 작으면 
                total_sale += amount

        # 조합된 하나의 할인율 턴이 끝나면 비교
        if max_plus < total_plus: # 플러스 서비스 가입자가 max 보다 크다. 
            max_plus = total_plus
            max_sale = total_sale
        elif max_plus == total_plus: # 플러스 서비스 사용자가 max와 동일하다. 
            if max_sale < total_sale: # 판매액이 max보다 크다. 
                max_sale = total_sale

    return [max_plus, int(max_sale)]


print(solution([[40, 10000], [25, 10000]], [7000, 9000]))