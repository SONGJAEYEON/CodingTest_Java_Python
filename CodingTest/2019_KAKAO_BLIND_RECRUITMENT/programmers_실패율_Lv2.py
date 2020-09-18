#실패율 : 스테이지에 도달했으나 아직 클리어 하지 못한 플레이어의 수 / 스테이지에 도달한 ㅡㄹ에이어의 수
#전체 스테이지 개수 n
#게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages
#실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 리턴하자!!

N=4 # 전체 스테이지의 수
stages=[4,4,4,4,4]
#[2, 1, 2, 6, 2, 4, 3, 3] # 게임을 이용하는 사용자가 현재 멈춰있는 스테이지 번호가 담긴 배열
numOfUser=len(stages) #전체 유저의 넘버
import heapq as hq
failure=[]
before_False=0
#자 실패율을 계산해서 
for i in range(1,N+1):
    if i in stages:
        temp=list(map(lambda x:x>i,stages))
        cnt_False=temp.count(False) #이건 어차피 numOfUser-cnt_True임
        newValue=cnt_False-before_False
#         print(newValue,"/",(newValue+numOfUser-cnt_False))
        hq.heappush(failure,(newValue/(newValue+numOfUser-cnt_False)*-1,i))
        before_False=cnt_False
    else:
        hq.heappush(failure,(0,i))
# print(failure)      
answer=[hq.heappop(failure)[1] for _ in range(N)]
print(answer)