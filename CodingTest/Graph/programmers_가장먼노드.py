# #1번노드에서  가장 멀리 떨어진 노드의 갯수를 구하자!!!
# #https://jisun-rea.tistory.com/entry/python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Level3-%EA%B0%80%EC%9E%A5-%EB%A8%BC-%EB%85%B8%EB%93%9C-%EA%B7%B8%EB%9E%98%ED%94%84?category=765195
# 
# n=6
# vertex=[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
# # distance=[99999 for _ in range(n)]
# # vertex.sort() #여기서 시간초과가 살짝 걱정이긴한데 일단 간다!
# # route={}
# # for node in vertex:
# #     if node[0] in route:
# #         route[node[0]].append(node[1])
# #     else:
# #         route[node[0]]=[node[1]]
# # print(route)
# 
# #1. 딕셔너리에 노드별 연결정보를 넣는다
# #2. 효율성을 위해 deque를 사용한다
# #3. deque에 노드번호,깊이 정보를 한번에 삽입한다
# #4. chk배열은 -1로 초기화하여 준비하고 인접노드를 탐색할 땐 한번 deque에 넣은 노드는 0으로 체크한다
# #(0으로 체크를 안해주면 이미 탐색한 노드를 재탐색함)
# 
# #5. 큐에서 꺼내올때 chk[노드번호]=깊이 로 넣어준다
# #6. 마지막으로 chk배열에서 최댓값을 카운트 해주면 된다.
# from collections import deque
# route={}
# for e1, e2 in vertex:
#     route.setdefault(e1, []).append(e2)
#     route.setdefault(e2,[]).append(e1) #양방향이라서 이렇게햇구남,,, 
# print(route)
# # route={}
# # for e1,e2 in vertex:
# #     if e1 in route:
# #         route[e1].append(e2)
# #     else:
# #         route[e1]=[e2]
# # print(route)
# print(vertex)
# q=deque([[1,0]])#첫번째 시작노드는 1이고 깊이는 0이기 때문에 이렇게 초기화함
# # q=[[1,0]]
# chk=[-1]*(n+1)
# while q:
#     idx,depth=q.popleft()
#     chk[idx]=depth
#     for i in route[idx]:
#         if chk[i]==-1:
#             chk[i]=0
#             q.append([i,depth+1])
#             print(chk)
#             print(q)
#             print()
#     depth+=1
# print(chk)
# print(chk.count(max(chk)))

# n=6
# vertex=[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
# def solution(n, vertex):
#     node={}
#     for v1,v2 in vertex:
#         node[v1]=node.get(v1,[])+[v2]
#         node[v2]=node.get(v2,[])+[v1] #간선이 양방향이기 때문에 이렇게 해서 딕셔너리에 저장하자!!
#     distance={i: float('inf') if i!=1 else 0 for i in range(1,n+1)}
#     from collections import deque
#     queue = deque([1]) #1에서부터 거리를 찾고있으니까 1을 출발점으로 고고!!
#     while queue:
#         nowPosition=queue.popleft()
#         for nextPosition in node[nowPosition]:
#             if distance[nextPosition]>distance[nowPosition]+1:
#                 distance[nextPosition]=distance[nowPosition]+1
#                 queue.append(nextPosition)
#     answerList=list(distance.values())
#     return answerList.count(max(answerList))
#     
# print(solution(n, vertex))


n=6
vertex=[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]