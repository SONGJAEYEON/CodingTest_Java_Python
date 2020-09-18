m=6
n=5
puddles=[[3,3]]
answer=0
# #노드별경우의 수를 구해 정답을 입력하는 배열
# 
# #길이 모두 정상일때의 경우의 수 
# #시발 왜틀리지? 
# for i in range(1,n):
#     for j in range(1,m):
#         route[i][j]=route[i-1][j]+route[i][j-1]
# # for r in route:
# #     print(r)
# flooded=0
# for i,j in puddles:
#     flooded+=(route[i-1][j-1]*route[n-i][m-j])
# # print(flooded) #얘가 답이 60이 나와서 
# # print((route[-1][-1]-flooded)%1000000007)#총 답이 66이 나와야함,,,!!

route = [[0]*(m + 1) for _ in range(n + 1)]
dp = [[0]*(m + 1) for _ in range(n + 1)]
for r in range(1, n + 1) :
    for c in range(1, m + 1) :
        if r == 1 and c == 1 : #윗줄이 싹다 0이니까 1,1로 시작해도댐,,,
            route[r][c] = 1
            #print(r," ",c)
            continue #이 컨티뉴의 존재의미를 잘 모르겠어,,, 어떡하지,,,
        if [c, r] in puddles : #오호,,! 이렇게 비교하니까 그냥 차라리 리스트 한줄씩 더 만드는게 낫겟네,,!!
            route[r][c] = 0
            continue # 컨티뉴가 진짜 쌉 중요한 포인트였네 여기서는,,, 
        route[r][c] = route[r -1][c] + route[r][c-1] 
        #여러개 for문을 쓰지않고 한 for문안에서 연산이 이루어질 수 있게 하려고 continue를 쓴거구나,,!! 
answer = route[n][m] % 1000000007
print(answer)

#와,, 한줄씩 더 만드니까 좋은점이
#인덱스마다 -1이런거 안해줘도 되고 (연산횟수 줄겟네,,,)
#하나씩 찾아갈 수 있었고(읭 이게 특징인가 그냥 ㅣㅇ 풀이의 특징같은데,,)
#하나의 for문에 continue를 써서 여러 연산을 차근차근 했다는게 상당히 인상깊었음
#나는 막 쫙 1 이렇게 초기화 하고 시작했는데,,!! 그냥 외운 풀이와 생각하는 풀이의 차이일까,,
#생각해보면 저렇게 푸는게 확률통계에서도 저런 사고과정이 있었기에 그런 공식이 나온거같은 늭김,,,ㅎ