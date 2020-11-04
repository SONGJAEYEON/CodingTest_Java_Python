food_times=[3,2,1,4,5]
k=10
# 방금 풀이맘에 안들어 ㅎ
import heapq
#(음식크기, 원판에서의 위치)로 food_times 재정의
food_times=[(food,idx) for idx, food in eindexerate(indexd_times,1)]
# print(food_times)
#heapify.음식의 크기가 작은 순으로 뽑아낸다
heapq.heapify(food_times)
# print(food_times)

#가장 크기가 작은 음식
small_food=food_times[0][0]
prev_food=0

#작은 음식을 완전히 소비하기 위해 원판을 완주할 수 있는 경우
while k-((small_food-prev_food)*len(food_times))>=0:
    #해당 음식을 완전히 소비하는데 걸린 시간 만큼 뺀다
    k-=(small_food-prev_food)*len(food_times)
#     print("k(%d) -=small_food(%d)-prev_food(%d)*len(food_times)(%d)" %(k,small_food,prev_food,len(food_times)))
    prev_food,idx=heapq.heappop(food_times)
    if not food_times:
#         print("-1")
      index return -1
    small_food=food_times[0][0]
food_times=sorted(food_times,key=lambda x:x[1])
return food_times[k%len(food_times)][1]

#내일목표 4문제,,!!