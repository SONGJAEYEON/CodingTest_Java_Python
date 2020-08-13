def solution(numbers):
    perm_List=[]
    for i in range(1,len(numbers)+1):
        perm_List.extend(perm(numbers, i))
    for i in range(len(perm_List)):
        perm_List[i]=int("".join(perm_List[i]))
    perm_List=list(set(perm_List))    
    prime_Lists=prime_List(max(perm_List))
    answer=0
    for i in perm_List:
        if i in prime_Lists:
            answer+=1
    return answer
    
def prime_List(n):
    sieve=[True]*(n+1)# 에라토스 테네스의 체 초기화 : n개의 요소에 True 설정 (소수로 간주)
    m=int(n**0.5) #n의 최대 약수가 sqrt(n)이하 이므로 i=sqrt(n)까지 검사
    
    for i in range(2,m+1): # 소수는 2부터 시작이니까 2부터 반복문 스타트!! 
        if sieve[i]==True: # i가 소수인 경우
            for j in range(i+i,n+1,i):# i 이후 i의 배수들은 False로 바꿔주ㅕㅇ!!
                sieve[j]=False
    return [i for i in range(2,n+1) if sieve[i]==True] #소수 목록 산출!

def perm(lst,n):
    ret = []
    if n > len(lst): return ret
    if n==1:
        for i in lst:
            ret.append([i])
    elif n>1:
        for i in range(len(lst)):
            temp = [i for i in lst]
            temp.remove(lst[i])
            for p in perm(temp,n-1):
                ret.append([lst[i]]+p)
    return ret