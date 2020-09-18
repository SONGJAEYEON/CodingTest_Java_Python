n=5 #선수의 수 
results=[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
# 내코드
# win={}
# lose={}
# score=[[0,0] for _ in range(n+1)]
# for a,b in result:
#     if a in win:
#         win[a].append(b)
#         score[a][0]+=1
#     else:
#         win[a]=[b]
#         score[a][0]+=1
#     if b in lose:
#         lose[b].append(a)
#         score[b][1]-=1
#     else:
#         lose[b]=[a]
#         score[b][1]-=1
# print(win)
# print(lose)
# print(score)

# 
# #세상에 회사는 많고 
# loseMember=list(map(lambda x:len(win[x]),list(win.keys())))
# print(loseMember)

# from collections import defaultdict 파이썬 컬렉션 진짜 종류많다... 
# https://itchallenger.tistory.com/58

#각 선수가 이긴선수와 진 선수 방법을 해쉬로 정리하고 한 선수의 win 정보 길이와 lose정보 길이를 합쳤을때 n-1과 같아지면 그 선수의 순위를 ㅏㄹ게된다
# 또한 실력의 차이가 극명해서 실력이 낮은 사람이 높은 사람을 이길 수 없다고 한다 (미친 이언니 천재네) 개똑똑하네
# 따라서 정보를 가지고있지않지만 이 조건들을통해서 정보를 다시 얻을 수있게 된다

#다른사람코드
#https://codedrive.tistory.com/190
answer=0
win={}
lose={}
for i in range(1,n+1):
    win[i]=set()
    lose[i]=set()
results.sort()

for i in range(1,n+1):
    for result in results:
        if result[0]==i:
            win[i].add(result[1])
        if result[1]==i:
            lose[i].add(result[0])# 여기서 승패를 기록하고!!!
            #set은 update 랑 add쓰는거 익혀두자!!!
    for j in win[i]:#와 요기 
        lose[j].update(lose[i]) # 개멋져
    for j in lose[i]:
        win[j].update(win[i])
for i in range(1,n+1):
    if len(win[i])+len(lose[i])==n-1:
        # 뽀인뜨!!!!
        answer+=1
print(win)
print(lose)
print(answer)
