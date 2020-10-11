#1 스택문제하나
#임시 메일 보관함을 구현하는 문제로 메일 송수신 및 사용자의 명령 레코드가 인풋으로 주어졌고
#이 레코드 대로 진행된 결과를 출력해야한다 
#receive는 임시보관함에 수신된 메일들을 저장하고 
#save는 ...ㅇㅋ 
from _operator import index

#2 
#연속된 2개이상의 숫자들을 더하여 나올수있는 모든 숫자를 오름차순으로 정리한 수열이 주어졌다.
#이 숫자
# https://www.acmicpc.net/problem/2337
#정점의 개수가 n인 트리의 간선을 자르는 과정을 반복하여 크기가 m인 트리를 얻어내려 한다. 
#이때 잘라야하는 간선의 최소개수를 구해내는 프로그램을 작성하시오
# node_list = {1: [2, 3], 6: [1], 7: [6],8: [6], 5: [3], 4: [3]}

# https://www.acmicpc.net/problem/1772
#정원 정리하기

# https://www.acmicpc.net/problem/2206
# 벽 부수고 이동하기4

#분해반응

#2 큐 문제 하나 

#3 그래프문제하나 

#4 그래프 문제 둘

#5 다이나믹프로그래밍하나? 분할정복? 그리디? 

#6 다이나믹프로그래밍하나? 분할정복? 그리디?

#결국,,,,
#====단어 변환 =====================
#
# begin="hit"
# target="cog"
# words=["hot", "dot", "dog", "lot", "log", "cog"]
# 
# def trans(a,b):
#     return sum((1 if x!=y else 0) for x,y in zip(a,b))==1 #이게
# 
# dict={}
# dict[begin]=set(filter(lambda x: trans(x, begin),words))
# for word in words:
#     dict[word]=set(filter(lambda x:trans(x,word),words))
# print(dict) #키 값에서 하나씩만 차이 나는애들 찾아줌!!!!
# from collections import deque
# queue=deque([(begin,0)])
# print(queue)
# # queue=deque([4,5,6])
# # queue.append(7)
# # queue.popleft()
# while queue:
#     now,level=queue.popleft() #이렇게 해야 빠르대!!! 
#     print(now," ",level)
#     if level>len(words):
#         print(0)
#         break
#     for word in dict[now]:
#         if word==target:
#             print(level+1)
#             break
#         else:
#             queue.append((word,level+1)


# m="kkaxbycyz"
# k="abc*"
# from collections import deque
# # k_deq=deque(k)
# answer=""
# size=len(k)-1
# i=0
# while 1:
#     if i==size:
#         answer="".join([answer,m])
#         print(answer)
#         break
#     if k[i] in m:
#         idx=m.index(k[i])
#         answer="".join([answer,m[:idx]])
#         print("answer ",answer)
#         i+=1
#         m=m[idx+1:]


#===============================
# blocks=[[0, 50], [0, 22], [2, 10], [1, 4], [4, -13]]
# answer=[[101 for j in range(i)] for i in range(1,len(blocks)+1)]
# i=0
# for a,b in blocks:
#     answer[i][a]=b
#     i+=1
# print(answer)
# 
# #이건 무조건 재귀!
# 
# def sum

# blocks    result
# [[0, 50], [0, 22], [2, 10], [1, 4], [4, -13]]    [50, 22, 28, 4, 18, 10, 0, 4, 14, -4, 1, -1, 5, 9, -13]


# [[0, 92], [1, 20], [2, 11], [1, -81], [3, 98]]    [92, 72, 20, 63, 9, 11, 144, -81, 90, -79, 217, -73, -8, 98, -177]

# blocks=[[0, 50], [0, 22], [2, 10], [1, 4], [4, -13]]
# answer=[[101 for j in range(i)] for i in range(1,len(blocks)+1)]
# size=sum(list(map(lambda x:len(x),answer)))
# print(size)
# print(size-len(blocks))
# i=0
# for a,b in blocks:
#     answer[i][a]=b
#     i+=1
# print(answer)

# for now,value in blocks:
#     if blocks[now][0]==0 :
#         top=
#         pass #왼쪽끝에있을때는 탑이랑 레프트만 보자!!
#     elif blocks[now][0]==now:
#         pass
#     else:
#     cri=answer[now][blocks[now][0]]
#     left=answer[now+1][blocks[now][0]]
#     right=answer[now+1][blocks[now][0]+1]
#     print(cri," ",left," ",right)
#     if cri!=101 and left!=101 and right==101:
#         answer[now+1][blocks[now][0]+1]=cri-left
#     elif left!=101 and right!=101 and cri==101:
#         answer[now][blocks[now][0]]=left+right
#     elif left==101 and right!=101 and cri!=101:
#         answer[now+1][blocks[now][0]]=cri-right
# 
#     cri=answer[now][blocks[now][0]]
#     left=answer[now+1][blocks[now][0]]
#     right=answer[now+1][blocks[now][0]+1]
#     print(cri," ",left," ",right)

# for i in range(1,len(answer)):
#     for j in range(len(answer[i])-1):
#         print(answer[i][j],end=" ")
#     print()
    
    
#     for j in range(len(blocks[i])-1):
#         print(answer[i][j],end="")
#     print()


# def cal(top,left,right):
#     if top!=101 and left!=101 and right==101:
#         pass # right를 계산할 수 있다!!
#     elif left!=101 and right!=101 and top==101:
#         pass # top계산!
#     elif left==101 and right!=101 and top!=101:
#         pass #t left계산 !



# str=["aabab","dog","aa","baaaa"]
S="aabab"
size=len(S)
total=sum(list(map(lambda x: 1 if x!='a' else 0 ,S)))
print(total)       



















    
