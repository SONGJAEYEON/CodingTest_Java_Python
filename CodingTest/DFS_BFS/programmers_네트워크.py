# n    computers    return
# 3    [[1, 1, 0], [1, 1, 0], [0, 0, 1]]    2
# 3    [[1, 1, 0], [1, 1, 1], [0, 1, 1]]    1


n=3
computers=[[1, 1, 0], [1, 1, 0], [0, 0, 1]]

def solution(n,computers):
    

# computer=[[1,1,0,1,0],[1,1,0,1,0],[0,0,1,0,1],[1,1,0,1,0],[0,0,1,0,1]]
# 
# #맨처음에 스타트하는 스택의초기화를 해야해!!
# n=5 #노드의 개수
# chk=[False for _ in range(n)]
# stack=[] # 여기에 이제 쌓을꺼야!!
# now=0
# network=0
# 
# chk=[False for _ in range(n)]
# stack=[]
# now=0
# network=0
# while(True):
#     flag=False # 해당 노트에서 갈수 있는 포인트가 있었다는걸 알려주기위한 플래그!
#     for node in range(n):
#         if computer[now][node]==1 and chk[node]==False: # 현재위치에서 갈 수 있는 포인트가 있다면!
#             stack.append(node)#갈 수 있는 포인트를 스택에 push해주고!
#             chk[node]=True #방문했다는 의미로 True로 바꿔주고
#             flag=True #뭐라도 찾을 수 있었다는 의미로 True로 바꿔주고
#     if flag==False: #갈 곳이 없었다면!
#         if len(stack)!=0: #지금까찌 찾았던 출발지중에서
#             now=stack.pop() #가장 끝에있는애를 새 출발지로 엮어주고!!
#         else : 
#             network+=1
#             if chk.count(True)<n:
#                 now=chk.index(False)
#             else:
#                 break
# print(network)        
