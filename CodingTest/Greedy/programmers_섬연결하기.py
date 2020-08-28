#자 크루스칼로 조져보자!!

# costs=[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
# n=4
n=6
costs = [[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]]
# 답 11

costs.sort(key=lambda x:x[2])
print(costs)
route=set([costs[0][0]])
print(route)
answer=0
while len(route)!=n:
    for i,cost in enumerate(costs):
        if cost[0] in route and cost[1] in route:
            #그래프가 만들어지는 조건을이렇게 해결했는데 어떤원리로 돌아가는지 알아보자!!! 
            continue
        if cost[0] in route or cost[1] in route:
            route.update([cost[0],cost[1]]) #아 업데이트라는함수가 합집합을만들어서 원본데이터를 갱신하는 메소드이구나
            #이렇게 했다는거 너무 놀랍고,,, 너무멋잇고,,, 감사함니다,,
            print(route)
            answer+=cost[2]
            costs[i]=[-1,-1,-1]
            break
print(answer)

# costs.sort(key=lambda x:x[2])
# print(costs)
# nodeChk=[False for i in range(n)] #노드를 방문했는지 안했는지 체크할 리스트
# minCost=0
# for cost in costs:
#     if nodeChk[cost[0]]==True and nodeChk[cost[1]]==True:#이 조건이 잘못되었네
#         #그래프를만드는 간선이라는 걸 판단하는 조건식을 어뜨케 만들 수 있을까요,,,
#         pass
#     else:
#         nodeChk[cost[0]]=True
#         nodeChk[cost[1]]=True
#         minCost+=cost[2]
#         print(nodeChk)
#         print(minCost)
# print(minCost)  

