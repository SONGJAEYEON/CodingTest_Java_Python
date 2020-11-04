from collections import deque
# N=5    
# road=[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
# K=3
# nodes={}
# dist={i : float('inf') if i!=1 else 0 for i in range(1,N+1)}
# for v1,v2,d in road:
#     nodes[v1] = nodes.get(v1, []) + [(v2, d)]
#     nodes[v2] = nodes.get(v2, []) + [(v1, d)]
#     print(nodes)
# que=deque([1])
# print(dist)
# print(nodes.get(1))
# print()
# while que:
#     cur_node = que.popleft()
#     for nxt_node, d in nodes[cur_node]:
#         if dist[nxt_node] > dist[cur_node] + d:
#             dist[nxt_node] = dist[cur_node] + d
#             que.append(nxt_node)
#         
#         print(dist)
#         print()
# print(len([True for dist in dist.values() if dist <= K]))

# 
# dict={}
# for v1, v2 ,weight in road:
#     dict[v1]=dict.get(v1,[])+[(v2,weight)]
#     dict[v2]=dict.get(v2,[])+[(v1,weight)] #이렇게 양방향으로 설정해주고
# distance={i:float('inf') if i!=1 else 0 for i in range(1,N+1)}
# from collections import deque
# queue=deque([1]) #무조건 1에서 출발하니까 1 일단 넣어주고 시작!! 
# while queue: # 더 이상 갈 곳이 없을 때 까지 반복문 궈궈~~
#     nowPosition=queue.popleft()
#     for nextPosition,weight in dict[nowPosition]:
#         if distance[nextPosition]>distance[nowPosition]+weight:#내가 더 짧은 루트라면~
#             distance[nextPosition]=distance[nowPosition]+weight
#             queue.append(nextPosition)
# # return len(list(filter(lambda x:x<=K,distance.values())))
# 
# print(len(list(filter(lambda x:x<=K,distance.values()))))

N=5    
road=[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K=3
def solution(N, road, K):
    dict={}
    for v1,v2,weight in road: 
        dict[v1]=dict.get(v1, [])+[(v2,weight)]
        dict[v2]=dict.get(v2, [])+[(v1,weight)]
    #1번마을에서 출발해서
    distance={i:float('inf') if i!=1 else 0 for i in range(1,N+1)}
    from collections import deque
    queue = deque([1])
    while queue:
        now=queue.popleft()
        for next,weight in dict.get(now):
            if distance[next]>distance[now]+weight:
                distance[next]=distance[now]+weight
                queue.append(next)
    return len(list(filter(lambda x :x<K,distance.values())))
                
    
print(solution(N, road, K))





















