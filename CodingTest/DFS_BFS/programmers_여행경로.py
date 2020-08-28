# https://scarletbreeze.github.io/articles/2019-08/%EA%B3%A0%EB%93%9D%EC%A0%90%ED%82%A4%ED%8A%B8(DFS,BFS)

tickets=[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

tickets.sort()
print(tickets)
route={}
tickets.sort()
for t1,t2 in tickets:
    if t1 in route:
        route[t1].append(t2)
    else:
        route[t1]=[t2]
print(route)#자 이렇게 해시테이블 만들고나면

#바로 answer로 갈 수는 없는건가!
stack=["ICN"]
answer=[]
print(answer)
while stack:
    now=stack[-1]
    if now not in route or len(route[now])==0:
        #now에서 출발해서 갈 수 있는루트가 없거나, now에서 출발하는 티켓을 모두 썼다면
        answer.append(stack.pop())
    else:
        stack.append(route[now].pop(0)) # 빼서 answer에 넣고 
answer.reverse()
print(answer)
    
#[ICN, ATL, ICN, SFO, ATL, SFO]
# case : [[ICN, A], [A, C], [A, D], [D, B], [B, A]]
# return : [ICN, A, D, B, A, C]
# 테스트케이스 2.
# ['ICN' ,'B'], ['ICN', 'C'] ,['C', 'D'], ['D', 'ICN']
# 
# -> ['ICN', 'C', 'D', 'ICN', 'B']
# 
# 테스트케이스 1.
# ['ICN', 'B'], ['B', 'C'], ['C', 'ICN'], ['ICN', 'D'], ['ICN', 'E'], ['E', 'F']
# 
# -> ['ICN', 'B', 'C', 'ICN', 'E', 'F', 'G', 'D']
#릴카 키? 170?
        

