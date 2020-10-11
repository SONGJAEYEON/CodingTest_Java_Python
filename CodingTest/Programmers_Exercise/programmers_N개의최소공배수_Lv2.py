# https://eda-ai-lab.tistory.com/491

arr=[1,2,3]
# arr.sort()
# num_set=set()
# for ele in arr:
#     for i in range(1,ele):
#         if ele%i==0 :
#             num_set.add(i)
# answer=1
# if len(list(num_set))==1:
#     for i in arr:
#         answer *= i
# else:
#     for j in list(num_set):
#         answer*= j
# 
# print(answer)

#와졸라 바로 틀렸어 ㅎ

#문제풀이 
#1. 내림차순으로 arr정렬
#2. 앞에서 부터 2개씩 즉 arr[i]과 arr[i+1]의 최소공약수를 찾고 그로부터 최소공배수를 계산하여 arr[i+1]에 넣음
#3. arr의 맨 마지막 원소가 전체 arr의 최소공배수 

#gcd라이브러리를 사용할 수 도 ㅣㅇㅆ음!! 
# arr=[2,6,8,14]
# arr.sort(reverse=True)
# for i in range(len(arr)-1):
#     a=arr[i] 
#     b=arr[i+1]
#     while a%b:
#         r=a%b
#         print(r)
#         a=b
#         b=r
#     arr[i+1]=(arr[i]*arr[i+1])/b
#     print(arr)
# print(arr[-1])


# https://brownbears.tistory.com/454

# from math import gcd
# arr=[2,6,8,14]
# answer=1
# for i in arr:
#     before=answer
#     answer=int(answer/gcd(answer, i))*i
#     
#     print(before," ",i," ",gcd(answer,i)," ",answer)
# print(answer)
