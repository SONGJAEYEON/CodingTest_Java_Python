#https://jjluveeecom.tistory.com/13?category=370124
# 오우 이 징검다리는 좀 심각해 진짜 모르겠어
# 이분탐색문제에서 어떤것을 이분탐색의 기준으로 삼을지 판단해야한다.
# 이 문제에서는 돌과 돌사이의 거리가 그 기준이다 
# 돌과 돌 사이의 거리는 rocks[1]-prev값이다.
#min_inter값은 리턴되는 값을 구하기위해 간격들의 최소값을 구하기위한 변수이다. math_inf는 무한데 값으로 최소값을 구하기위한 초기값을 넣어두는 것이다

distance=25
rocks=[2, 14, 11, 21, 17]
n=2
import math

answer=0
start,end=0,distance
rocks=sorted(rocks)
rocks.append(distance)
rnum=len(rocks)

while start<=end:
    remove=0
    prev=0
    min_inter=math.inf
    mid = (start+end)//2

    for i in range(rnum):
        if rocks[i]-prev < mid:  #rocks[i]-prev가 inter값
            remove+=1 #바위제거
            
        else : #바위 제거 안할경우 
            min_inter=min(min_inter,rocks[i]-prev) #inter값 갱신.
            prev=rocks[i] #현재 바위위치를 prev로

    #너무 많이 제거되었을 경우, 기준을 높여서 제거를 줄여야함
    if remove > n:
        end=mid-1
    #적게 제거되었을 경우, 기준을 낮춰서 제거를 늘려야함
    else:
        answer=min_inter
        start=mid+1
print(answer)
    
        