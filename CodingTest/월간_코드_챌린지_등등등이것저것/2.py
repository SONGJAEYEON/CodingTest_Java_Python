# arr=[[1,1,1,1,1,1,1,1],
#      [0,1,1,1,1,1,1,1],
#      [0,0,0,0,1,1,1,1],
#      [0,1,0,0,1,1,1,1],
#      [0,0,0,0,0,0,1,1],
#      [0,0,0,0,0,0,0,1],
#      [0,0,0,0,1,0,0,1],
#      [0,0,0,0,1,1,1,1]]

# arr    result
# [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]    [4,9]
# [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]    [10,15]

# arr=[[1,1,0,0],
#      [1,0,0,0],
#      [1,0,0,1],
#      [1,1,1,1]]
# from math import log2
# print(int(log2(len(arr[0])))) #잘라볼수 있는 횟수,,? 
# 
# #(0,0) (3,3) startx starty endx endy
# #(1/1)
# # 이것은 무조건 재귀다,,,ㅎ
# #half=3//2
# #1 (0,0) (half,half)
# #2 (0,half+1) (endx,half)
# #3 (half+1,0) (endx,half)
# #4 (half+1,half+1) (endx,endy)


# arr=[[1,1,1,1,1,1,1,1],
#      [0,1,1,1,1,1,1,1],
#      [0,0,0,0,1,1,1,1],
#      [0,1,0,0,1,1,1,1],
#      [0,0,0,0,0,0,1,1],
#      [0,0,0,0,0,0,0,1],
#      [0,0,0,0,1,0,0,1],
#      [0,0,0,0,1,1,1,1]]

arr=[[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]

# def quad(x1, y1, x2, y2, n) :
#     if n == 1 :
#         return arr[y1][x1] 
#     a = n // 2
#     # 4등분으로 분할    
#     r1 = str(quad(x1, y1, x1+a, y1+a, a)    )
#     r2 = str(quad(x1+a,y1, x1+n, y1+a, a)   )
#     r3 = str(quad(x1, y1+a, x1+a, y1+n, a)  )
#     r4 = str(quad(x1+a, y1+a, x1+n, y1+n, a))    
#     # 모두 같은 값일 경우 하나만 출력
#     if r1==r2==r3==r4 and len(r1) == 1 :
#         return r1
#     return r1 + r2 + r3 + r4
# def solution(arr):
#     X = len(arr)
#     answer=quad(0,0,X,X,X)
#     return [answer.count("0"),answer.count("1")]
# 
# print(solution(arr))








A=[5,1,3,7]
B=[2,2,6,8]
import heapq
heapq.heapify(A)
heapq.heapify(B)
cnt=0
# for a in range(len(A)):
while A:
    if heapq.heappop(A)<heapq.heappop(B):
        cnt+=1
print(cnt)


















