#1번노드에서  가장 멀리 떨어진 노드의 갯수를 구하자!!!
#https://jisun-rea.tistory.com/entry/python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Level3-%EA%B0%80%EC%9E%A5-%EB%A8%BC-%EB%85%B8%EB%93%9C-%EA%B7%B8%EB%9E%98%ED%94%84?category=765195

n=6
vertex=[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
# distance=[99999 for _ in range(n)]
# vertex.sort() #여기서 시간초과가 살짝 걱정이긴한데 일단 간다!
# route={}
# for node in vertex:
#     if node[0] in route:
#         route[node[0]].append(node[1])
#     else:
#         route[node[0]]=[node[1]]
# print(route)

#1. 딕셔너리에 노드별 연결정보를 넣는다
#2. 효율성을 위해 deque를 사용한다
#