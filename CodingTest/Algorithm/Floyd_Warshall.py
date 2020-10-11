# https://it-garden.tistory.com/247?category=845076

#플로이드와샬 알고리즘은 모든 정점사이의 최단 경로를 찾는 탐색 알고리즘 입니다

# 플로이드 워셜 알고리즘의 과정입니다

# 하나의 정점에서 다른 정점으로 바로갈 수 있으면 최소비용을, 갈 수 없다면 INF로 배열에 값을 저장합니다

# 3중 FOR문을 통해 거쳐가는 정점을 설정한 후 해당 정점을 거쳐가서 비용이 줄어드는 경우이는 값을 바꿔줍니다

# 위의 과정을 반복하여 모든 정점 사이의 최단경로를 탐색합니다

import sys

INF = sys.maxsize

def Floyd_Warshall():
    dist = [[INF]*n for i in range(n)] # 최단 경로를 담는 배열

    for i in range(n): # 최단 경로를 담는 배열 초기화
        for j in range(n):
            dist[i][j] = a[i][j]

    for k in range(n): # 거치는 점
        for i in range(n): # 시작점
            for j in range(n): # 끝점
                # k를 거쳤을 때의 경로가 더 적은 경로
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
        for X in range(n):
            for Y in range(n):
                print(dist[X][Y],end=' ')
            print()
        print()
    return dist

n = 4 # 정점 수
a = [[0, 2, INF, 4],[2, 0, INF, 5],[3, INF, 0, INF],[INF, 2, 1, 0]]
# print()
# for X in range(n):
#     for Y in range(n):
#         print(a[X][Y],end=' ')
#     print()

dist = Floyd_Warshall()

print("========================")
for X in range(n):
    for Y in range(n):
        print(dist[X][Y],end=' ')
    print()