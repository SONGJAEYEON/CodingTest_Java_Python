# 제한 사항 이 문제의 풀이가 너무 궁금해,,,, 
# n은 3 이상 250,000 이하입니다.
# edges의 행의 개수는 n-1 입니다.
# edges의 각 행은 [v1, v2] 2개의 정수로 이루어져 있으며, 이는 v1번 정점과 v2번 정점 사이에 간선이 있음을 의미합니다.
# v1, v2는 각각 1 이상 n 이하입니다.
# v1, v2는 다른 수입니다.
# 입력으로 주어지는 그래프는 항상 트리입니다.
# 
# n    edges    result
# 4    [[1,2],[2,3],[3,4]]    2
# 5    [[1,5],[2,5],[3,5],[4,5]]    2
# 
# f값에 사용될 3개의 점으로 (1, 2, 3), (2, 3, 4) 등을 고를 때 가장 큰 값인 2를 얻을 수 있으므로, 2를 return 해야 합니다.



# A=
# #[3,2,-2,5,-3]
# 
# answer=0
# for a in A:
#     if (-1*a in A) and answer<=a:
#         answer=a
# print(a)
#         
                   

N=6
NList=[-i for i in range(N-1)]
print(NList)
NList.append(abs(sum(NList)))
print(NList)