def solution(cap, n, deliveries, pickups):
    answer = -1
    deliveries = [0] + deliveries
    pickups = [0] + pickups

    will_delivery_total = sum(deliveries) # 배달 해야하는 총 개수

    # 창고에서 트럭에 짐 싵기
    def start_truck(total):
        if total > cap:
            return total - cap
        else:
            return total
    # deliver max 값 도 확인해 볼것 -> 갱신하는 내용 추가
    # deliver 최장 거리 부터 빼는 함수
    def after_deliver(last_house, deliver_truck): # 들러야 하는 가장 먼집, 트럭의 짐
        max_i = 0
        max_house = last_house
        for i in range(last_house,0,-1): # 가장 멀리 있는 것 부터 체크

            if deliveries[i]:
                if not max_i:
                    max_i = i

                if deliver_truck >= deliveries[i]:
                    deliver_truck -= deliveries[i]
                    deliveries[i] = 0
                    max_house = i
                    if deliver_truck == 0:
                        return max_i, max_house # 최장 거리, 확인 하면 되는 delivery

                else:
                    deliveries[i] -= deliver_truck
                    deliver_truck = 0
                    return max_i


        return max_i

    def after_pickup(last_house, pickup_truck):
        max_i = 0
        for i in range(last_house,0,-1):
            if pickups[i]:
                # todo :







    return answer

# 아직 구현중
'''
delivers-> 제일 먼 집부터 한다 
pickups도 제일 먼 집부터 한다. 
마지막 집을 끝내면 마지막집은 안가도 되는 구역을 바뀜

일단 배달을 먼저 한다. deliveries를 뒤에서 부터 빼준다.
truck = 4  (delivers_sum이 cap 보다 작은 경우 다 실어)
truck_p = 0
deliveris 값이 있으면 max_i 에 할당
길은 max_i -> 부터 뒤에서 값을 빼줌 truck = 0이 될때까지 delivers에 재할당 뺴준값으로
그리고 pickup을 살펴봐 pickup이 더 i 값을 더 크면 바꿔줌 작으면 안바꿔줌
그리고 pickup이 truk_p 될때까지 실어줘

이제 max_i *2 가 거리임 -> max_i 값 다 더해준 다음 *2




배달을 가면서 하면 됨
pickups를 확인 한다. 
'''