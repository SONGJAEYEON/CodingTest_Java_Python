'''
https://www.acmicpc.net/problem/11437
이 문제는 LCA(Lowest Common Ancestor)문제 이다.
이 문제는 depth를 모두 구하고 부모와 자식간의 관계를 구하여 트리를 만든 다음에
구하고자 하는 정점의 depth를 맞춰 준 다음 같은 노드가 될 때 까지 부모를 타고 하나씩 올라오면 됩니다.

6과 11의 lca를 구하는 것을 예로 들겠습니다.
부모 노드가 정해져 있지 않기 때문에 모든 노드ㅢ dfs를 돌면서 depth를 구합니다.
이때  depth가 0인 것은 depth를 아직 구하지 않은 노드이기 때문에 -> dfs를 물고 들어가서 depth를 update시켜 줍니다.
루트 노드인 1부터 출발합니다. 1과 연결된 점으로 우선 2가 있습니다.
그러면 2에는 465가 있습니다. 재귀로 들어왔기 때문에  4는 depth가 증가된 상태입니다.
4와 연결된 점 29가 있는데 2는 이미 depth를 구했고 9를 from값으로 들어갑니다.

이제 더이상 9와 연결된 점이 없습니다. (4는 이미 depth가 update됨)

그러면 이제 4가 from인 context로 돌아와서 9의 부모가 4가 됨을 알 수 있습니다.
4에 대해서 끝났고 from인 context로 돌아와소 6을 탐색하고 6의 부모는 2임을 update할 수 있습니다.
이와 같은 방식으로 depth를 가지고  부모와 자식간의 관계를 구할 수 있습니다.

이제 둘 중 depth가 더 작은 것에 기준을 맞춰서 depth를 같게해줍니다.
11의 depth가 더 크기 때문에 6에 맞추어 올려줍니다. 즉 11은 5로 바뀝니다.

그리고 depth를 하나씩 감소시키면서(위로 올라가면서) 같은 값이 나올때 까지 반복합니다.
6과 11에서 paranet를 이용해 하나씩 올리면 둘다 2가 나오면서 같게되고 이기 LCA가 됩니다.

자바 메모리 56580 시간 1576
파이썬 메모리 93584 시간 312 

'''
import sys
from functools import lru_cache
from collections import defaultdict
r=sys.stdin.readline
sys.setrecursionlimit(10**9)
N=int(r())
g=defaultdict(set)
for _ in range(N-1):
    a,b=map(int,r().split())
    g[a].add(b)
    g[b].add(a)
    #양방향 그래프 구성
tree=[-1]+[(0,0)]*N#1번~N번까지 부모,레벨 설정
print(tree)
#leafs=[]
def buildTree(parent):
    #if not g[parent]:
    #    leafs.append(parent)
    for node in g[parent]:
        tree[node]=(parent,tree[parent][1]+1)
        g[node].discard(parent) #모르는 메소드가 졸라많죠,,,ㅎ
        buildTree(node)
        #dfs로 그래프탐색하여 노드별 부모와 레벨 설정
buildTree(1)
print()
print(tree)
print(g)
# @lru_cache()
# def LCA(a,b):
#     if a==b:
#         return a
#     #기저사례
#     else:
#         if tree[a][1]>tree[b][1]:#b가 더 높은 레벨일경우
#             return LCA(tree[a][0],b)
#         elif tree[a][1]<tree[b][1]:#a가 더 높은 레벨일경우
#             return LCA(a,tree[b][0])
#         else:#레벨이 같은경우
#             return LCA(tree[a][0],tree[b][0])
#         
#         
# M=int(r())
# res=[]
# for _ in range(M):
#     a,b=map(int,r().split())
#     a,b=min(a,b),max(a,b)
#     res.append(LCA(a,b))
# for num in res:
#     print(num)