#창고에 재고로 쌓여있는 상품들을 
##1
# boxes=[[1, 2], [2, 3], [3, 1]]
# numOfBox=len(boxes) #박스의 개수 
# complete=0
# # pick=[]
# # boxes=[set(k) for k in boxes]
# cntDic=dict()
# for a,b in boxes:
#     if a in cntDic:
#         cntDic[a]+=1
#         if cntDic[a]>=2:
#             del(cntDic[a])
#             complete+=1
#     else:
#         cntDic[a]=1
#     if b in cntDic:
#         cntDic[b]+=1
#         if cntDic[b]>=2:
#             del(cntDic[b])
#             complete+=1
#     else:
#         cntDic[b]=1
# # print(cntDic)
# # print(complete)
# print(len(boxes)-complete)


################2

# 명령이 [6, 2, 5, 1, 4, 3]으로 주어진 경우, 다음과 같이 공이 빠져나오게 됩니다.
# 1. 6번 공은 오른쪽 끝에 있으므로 바로 빠져나옵니다.
#6번나와~ 어 너 끝에있네~ 응 나와~

# 2. 2번 공은 다른 공 사이에 있기 때문에 바로 나가지 못하고 보류 상태가 됩니다.
#2번나와 어 끼어있네 보류~

# 3. 5번 공은 6번 공이 빠져나갔기 때문에 오른쪽 끝에 있으므로 바로 빠져나옵니다.
#5번나와 오 나올수있네? 나와~

# 4. 1번 공은 왼쪽 끝에 있으므로 바로 빠져나옵니다. 보류 상태였던 2번 공이 이제 빠져나올 수 있기 때문에 뒤이어 2번 공이 빠져나옵니다.
#1번나와~ 2번나올수있어? 나와~ (나올때마다 보류한거 파악해줘야할듯,,?)

# 5. 4번 공은 오른쪽 끝에 있으므로 바로 빠져나옵니다.

# 6. 3번 공은 마지막 공이기 때문에 어느 쪽으로든 나올 수 있습니다.


# ball    order    result
# [1, 2, 3, 4, 5, 6]    [6, 2, 5, 1, 4, 3]    [6, 5, 1, 2, 4, 3]
# [11, 2, 9, 13, 24]    [9, 2, 13, 24, 11]    [24, 13, 9, 2, 11]
ball=[11, 2, 9, 13, 24]
order=[9, 2, 13, 24, 11]
result=[6, 5, 1, 2, 4, 3]


#자 2번만이라도 풀자!! 재귀 고고고고고!!!
answer=[]
hold=[]
def pickball(ball,order):
    while True:
        if not ball:
            return answer
#         elif not order: #이 조건을 수정해야함,,!! 
#             return answer
        else:
#             TopandBottom= [ball[0]] if len(ball)==1 else [ball[0],ball[len(ball)-1]]
            TopandBottom=[ball[0],ball[len(ball)-1]]
            print(ball," ",order," ",hold," ",answer," ",TopandBottom)
            now=order[0] #맨끝에있는거 보고
            if len(order)==0 and len(hold)==0:
                return answer
            elif len(order)==0 and len(hold)!=0:
                pickball(ball,hold)
            if now in TopandBottom:
                ball.remove(now)
                answer.append(now)
                order.pop(0)
                print("if  ",ball," ",order," ",answer," ",TopandBottom)
                pickball(ball,hold)
            else:
                hold.append(order.pop(0))
#                 print("else  ",ball," ",order," ",now," ",hold," ",answer," ",TopandBottom)
                print("else  ",ball," ",order," ",answer," ",TopandBottom)
print(pickball(ball, order))
print(result)
        

    
    



















