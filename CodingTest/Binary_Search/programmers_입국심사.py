#이진탐색 재귀로 구현해보자!!
from _ssl import OP_ENABLE_MIDDLEBOX_COMPAT

def binarySearch(arr,target,left,right):
    middle_idx=(left+right)//2
    print(middle_idx)
    middle=arr[middle_idx]
    if target==middle:
        print(middle_idx," ",middle)
    elif middle > target:
        binarySearch(arr, target,left,middle_idx-1)
    elif middle < target:
        binarySearch(arr, target,middle_idx+1,right)
    else: 
        return False
n=6
times=[7,10]
#[1,2,3,6,8]

#문제의 핵심은 최소, 최대 범위를 구한 뒤 구하려고하는 답을 이분탐색으로 범위를 좁혀가며 답을 구하는 것입니다
#문제에서 최대범위는 심사괸중 가장 오래걸리는 심사관을 계속 검사받는 경우입니다
#최대 최소 범위의 중간값인 mid가 n명을 심사할 수 있는지 아닌지를 파악하며 이분탐색을 진행합니다
#n명을 심사할 수 있다면 답을 갱신하고 최대범위를 줄여봅니다
# n명을 심사할 수 없다면 최소범위를 늘려봅니다 (오호,,!)
# https://wwlee94.github.io/category/algorithm/binary-search/immigration/
# answer=0
# howmany=len(times) #몇명의 감독관이 있는지! 
# left=1
# right=(howmany+1)*max(times) #최대범위
# 
# while left<=right:
#     mid=(left+right)//2
#     count=0
#     for time in times:
#         count+=(mid//time)
#         print(count)
#         if count>=n: break #심사 인원수를 넘으면 다음단계
#     #n명을 심사할 수 있는 경우 한 심사관에게 주어진 시간을 줄여본다
#     print()
#     if count >= n :
#         answer=mid
#         right=mid-1
#     #없는 경우 
#     else:
#         left=mid+1
# print(answer)

#풀이
# 우리가 구하고자 하는것 : 모든 사람이 심사를 받는데 걸리는 시간
# 1 답의 범위를 좁혀준다
# 모든 심사원의 일 처리 속도를 일처리가 제일 빠른 심사원 값으로 한 것보단 클 것이고 
# 모든 심사원의 일 처리 속도를 제일 일처리가 느린 심사원 갑승로 한 것보단 작을 것이다 

# 이분탐색을 이용해 답의 범위 안에서 만족하는 최소값을 구해낸다
# (nSum>n 이 아닌 nSum>=)이기 때문에 nSum==n이었을 때도 아래의 값을 보게되어 최소값을 구할 수 있다

#최소값을 찾는 이분탐색을 시작하시져~~
#이분탐색에서 전제조건은  정렬이 되어야한다!! 라는거양!!
# times.sort()
# start=times[0]*n/len(times) #7*6/2=21 #가장 작은시간으로 모두가 검사를 받는데 그 평균시간을 내기위해서 심사원 수로 나눠준건가?#근데 왜 나눠주는거야? 
# end=times[len(times)-1]*n/len(times) #10*6/2=30
# #나눠야함 근데 왜  나눠야하는지 모르겠어,,, 
# #아아,,, 이거 아무러케나 해도될듯,,!! 
# 
# #재귀에서 중요한것은 종료조건!! 
# def find(s,e): 
#     if s==e:#시작점과 종료점이 같다면
#         return s #시작점을 리턴해라 
#     mid = int((s+e)/2) #최소시긴과 최대시간의 중간점 중간시간!!/
#     nSum=0 #입국심사를 받은 사람의 수 
#     for time in times:
#         nSum+=mid//time #자 이제 이 수식을 찾아가야해,,
#         if nSum>n:
#             break
#     if nSum>=n:
#         return find(s,mid) #재귀로 구현한 이분탐색,,!! 
#     else:
#         return find(mid+1,e)

# https://jjluveeecom.tistory.com/12
answer=0
short=1
long=max(times)*n # 모든 숭객이 제일 일못하는 심사원한데 검사받았을때 시간!!
mid=(long+short)//2
nSum=0
while(short<=long):
    nSum=0
    mid=(long+short)//2
    for time in times:
        nSum+=(mid//time)
    if nSum<n:
        #명수가 적으면 오우 시간이 좀 즉나? 하면서 올려주고 
        short=mid+1
    else:
        long=mid-1 #명수가 많으면 시간 줄여도되니까 최장시간 건드려주고
        #이건 와일 종료조건에따라서 값 바뀌니까 그거때무넹 그런듯!! 
        answer=mid
        
































