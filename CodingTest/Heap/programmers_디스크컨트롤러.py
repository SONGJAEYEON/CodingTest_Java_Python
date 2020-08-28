#힙 어뜨케 쓰는지 다 까먹어따 조때따^^
# https://www.daleseo.com/python-heapq/
#답 참고
#https://seoyoung2.github.io/algorithm/2020/06/04/Programmers-diskcontroller.html
import heapq as hq
import time
from sqlite3 import Time
jobs=[[0, 3], [1, 9], [2, 6]]
count=0 #처리한 작업의 수 
last=-1 #최근에 끝난 작업시간
answer=0
jobs.sort()
#시작시간초기화
time=jobs[0][0] #총 작업시간
heap=[]
while count<len(jobs):
    for s,t in jobs:
        if last<s<=time: # 시발 이건 또 어디서나온 문법이래요??
            #작업요청시간이 최근에 끝난 작업시간보다 크고 총작업시간보다 작다면,,,(뒤에 조건 왜필요한거ㅣㅈ,,?)
            #작업소요시간으로 minheap을 만들기위해 (t,s)를 푸시한다
            hq.heappush(heap, (t,s))
    if len(heap)>0:#바로 수행할 수 있는 작업이 있는 경우
        count+=1 #일 하나했으니까 카운트 하나 올리고 
        last=time #작업시간 넣어줘서 지금 시간이 얼마나 흘렀는지 갱신해주고
        term,start=hq.heappop(heap) #힙에서 작업시간이랑 요청시간이랑 갖고와서
        time+=term # 전체작업시간에 현재 선택된 작업시간 넣어주고
        answer+=(time-start) #현재 작업의 요청시간 빼줘서 전체총합에 더하고~
    else:#바로 수행할 수 있는 작업이 없는 경우
        time+=1
print(answer//len(jobs))            
        



# def time_1(jobs):
#     total=0
#     time=0
#     for job in jobs:
#         total+=job[1]
#         time+=(total-job[0])
#     return time
# def time_2(jobs):
#     heap=[]
#     total=0
#     time=0
#     i=0
#     for job in jobs:
#         hq.heappush(heap, job[1])
#     while heap:
#         total+=hq.heappop(heap)
#         time+=(total-i)
#         i+=1
#     return time
# print(min(time_2(jobs),time_1(jobs))//len(jobs))
#하드 디스크가 작업을 수행하고있지않을때에는 먼저 요청이 들어온 작업부터 처리합니다 
# 이 제한사항을 어떻게 구현하면좋을까요,,, 

     
