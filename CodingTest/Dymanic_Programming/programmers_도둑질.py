money=[1,2,3,4,5,6,5,4,3,2,1]

# def solution(money):#일단 코드를 따라쳐보겠습니다
#     dp1=[0]*len(money)
#     dp1[0]=money[0]
#     dp1[1]=max(money[0],money[1])
#     
#     for i in range(2,len(money)-1): #첫집을 무조건 터는 경우
#         dp1[i]=max(dp1[i-1],money[i]+dp1[i-2])
#         
#     dp2=[0]*len(money)
#     dp2[0]=0
#     dp2[1]=money[1]
#     
#     for i in range(2,len(money)): #마지막 집을 무조건 터는 경우
#         dp2[i]=max(dp2[i-1],money[i]+dp2[i-2])
#     return max(max(dp1),max(dp2))
# 
# print(solution(money))

#상향식 동적계획법이라는 것이 뭘까아,,, ㅠ

def solution(money):
    cache = [money[0], money[0]] # 0번째 요소를 고르고 시작한 경우
    cache2 = [0, money[1]] # 0번째 요소를 고르지 않고 시작한 경우

    for i in range(2, len(money)-1):
        cache.append(max(cache[i-2] + money[i], cache[i-1]))

    for i in range(2, len(money)):
        cache2.append(max(cache2[i-2] + money[i], cache2[i-1]))

    return max(cache[-1], cache2[-1])