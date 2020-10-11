
nums=[1,2,7,6,4]

from itertools import combinations


nums_list=list(combinations(nums,3))
print(nums_list)

def prime_list(n):
    #구하고자 하는 수만큼 True를 갖는 리스트 생성
    primeChk=[True]*n
    for i in range(2,len(primeChk)):
            for j in range(i+i,n,i):
                primeChk[j]=False
    return primeChk

prime_Number=prime_list(3000)  
print(prime_Number)              
cnt=0
for combi in nums_list:
    if prime_Number[sum(combi)]:
        cnt+=1
print(cnt)    