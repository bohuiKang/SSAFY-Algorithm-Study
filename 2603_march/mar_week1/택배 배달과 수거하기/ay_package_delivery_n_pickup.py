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
'''
깔끔하게 정리한 내용

delivers 를 먼저 확인하고 pickups를 확인한다.
총 delivers 를 sum해서 총 배달 개수 확인한다.
총 pickups 를 sum해서 총 수거 개수를 확인한다.

cap 만큼 truck에 싣는다. (남은 배달해야 되는 개수가 cap보다 작으면 남은 배달 개수를 truck에 할당)
delivers를 뒤에서 부터 순회 하면서 값이 있으면 max_i에 가장 큰 인덱스 값 할당한다.
truck에 담긴 값 만큼을 delivers 뒤쪽 값부터 차례대로 빼준다. truck이 0이 될때까지

pickups 도 뒤에서 부터 순회 하면서 값이 있는 인덱스 값중 가장 큰 값을 할당한다. (뒤에서 부터 순회 하니까 제일 처음 값이 있는 인덱스 값)
truck = cap 할당 해놓고 truck에서 pickups 값 뒤쪽에서 부터 빼주고 truck 0 될때까지 해준다.

그리고 deliver 1번 순회 pickup 한번 순회를 한것을 전체 1회 순회라고 보고
1회 순회 때마다 deliver의 max_ i, pickups의 max_i 값을 비교하고 max 값을 total에 더해준다.
total은 마지막에 *2 해준 값이 최소 거리가 된다.

그리고 중간에 trucks =0 될때까지 순회하면서 delivers[i]=0, pickups[i]=0으로 바뀌는 경우 인덱스 값을 각각 기록해둔다. 
그래서 다음 순회 때는 해당 인덱스 값 부터 0인덱스 까지 순회하면 된다. (for 범위를 줄여주는 작업)

총 배달 개수, 총 수거 개수에서 순회하면서 값들 빼준면서 해당 값 모두 소진시 순회 멈추게 된다. (deliver나 pickup 중 하나만 소진 한 경우 나머지 순회는 진행)
'''