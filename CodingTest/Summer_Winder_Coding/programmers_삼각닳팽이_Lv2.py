n=5
#     [1, 2, 9, 3, 10, 8, 4, 5, 6, 7]
answer=[[0]*i for i in range(1,n+1)]
x,y,c,value=0,0,0,1
dx,dy=0,0
for direction in range(n,0,-1):
    if (n-direction)%3==0:
        #아래로 아래로~
#         print(direction," 아래로~")
#         print(x," ",y)
        for dx in range(direction):
            answer[x+dx][y]=value
            value+=1
        x+=dx    
#         print(answer)
#         print(x," ",y)
    elif (n-direction)%3==1:
#         print(direction," 옆으로~")
#         print(x," ",y)
        for dy in range(1,direction+1):
            answer[x][y+dy]=value
            value+=1
        y+=dy
#         print(answer)
#         print(x," ",y)
    else:
#         print(direction," 대각선위로~")
#         print(x," ",y)
        for c in range(1,direction+1):
            answer[x-c][y-c]=value
            value+=1
        x-=(c-1)
        y-=c
#         print(answer)
#         print(x," ",y)
result=[]
for an in answer:
    result.extend(an)
print(result)


# def solution(n):
#     a, x, y, c = [[0 for _ in range(i + 1)] for i in range(n)], -1, 0, 0
# 
#     for i in range(n, 0, -1):
#         for j in range(i):
#             x, y = (x + 1, y) if (n - i) % 3 == 0 else (x, y + 1) if (n - i) % 3 == 1 else (x - 1, y - 1)
#             a[x][y] = (c := c + 1)
# 
#     return [v for b in a for v in b]