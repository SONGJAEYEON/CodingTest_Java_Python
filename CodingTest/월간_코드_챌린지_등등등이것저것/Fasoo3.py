# 다른 자동차 한대가 방해되지 않도록 자동차 두대를 주차하는 방법의 개수를 return 

# parking    result
# [[1, 2],[3, 4],[-1, -1],[-1, -1],[-1, -1]]    4
# [[1,2],[3,4],[5,6],[-1,7],[8,9],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1]]    26
# parking=[[1,2],[3,4],[5,6],[-1,7],[8,9],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1]]
# 
# dict={}
# 
# for i,value in enumerate(parking):
#     if value[0]!=-1:
#         dict.setdefault(i, value[0])
#         dict.setdefault(value[0],i)
#     if value[1]!=-1:
#         dict.setdefault(i, value[1])
#         dict.setdefault(value[1],i)
# print(dict)
# 
# from itertools import combinations
# case=list(combinations([1,2,3],2))
# print(case)


#     for i in range(1,len(arr)-1):
#        if sum(arr[:i+1])==sum(arr[i:]):
#         return i

#대학은 교수 학과 과정 및 일정에 대한 데이터를 네가지 테이블로 유지합니다
#학과 밖에서 가르치는 과정의 이름과함께 교수이름을 인쇄하는 커리 
# professor.name course.name이 있어야함
#여러학기에 걸쳐 동일한 과정을 가르치는 교수는 한번만 표시되어야함

# 아 아니구나 모든 과정에서 0보다 작아지면 안되네!!
# arr=[-5,4,-2,3,1]
# start=0
# total=0
# i=0
# total+=start
# while i<len(arr):
#     total+=arr[i];
#     if total<0: 
#         start+=1
#         total=start
#         i=0
#     else:
#         i+=1
# # print(start+1)
# 
# n=26
# from collections import deque
# str=deque(['a','e','i','o','u'])
# next=[]
# end_A=['e']
# end_E=['a','i']
# end_I=['a','e','o','u']
# end_O=['i','u']
# end_U=['a']
# # for i in range(n):
# i=1
# ele=""
# while 1:
#     ele=str.popleft()
#     if len(ele)==n:
#         break
#     if ele[-1]=='a':
#         for a in end_A:
#             str.append(ele+a)
#         print(ele," ",str)
#     elif ele[-1]=='e':
#         for e in end_E:
#             str.append(ele+e)
#         print(ele," ",str)
#     elif ele[-1]=='i':
#         for i in end_I:
#             str.append(ele+i)
#         print(ele," ",str)
#     elif ele[-1]=='o':
#         for o in end_O:
#             str.append(ele+o)
#         print(ele," ",str)
#     else:
#         for u in end_U:
#             str.append(ele+u)
# #         print(ele," ",str)
#         
# print(str)
# print(len(str))

















