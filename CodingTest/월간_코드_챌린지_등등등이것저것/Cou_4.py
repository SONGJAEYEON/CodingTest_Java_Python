#4 경로의 수 구하기 
 
#case1
# depar="SEOUL"
# hub="DAEGU"
# dest="YEOSU"
# roads=[["ULSAN","BUSAN"],
#        ["DAEJEON","ULSAN"],
#        ["DAEJEON","GWANGJU"],
#        ["SEOUL","DAEJEON"],
#        ["SEOUL","ULSAN"],
#        ["DAEJEON","DAEGU"],
#        ["GWANGJU","BUSAN"],
#        ["DAEGU","GWANGJU"],
#        ["DAEGU","BUSAN"],
#        ["ULSAN","DAEGU"],
#        ["GWANGJU","YEOSU"],
#        ["BUSAN","YEOSU"]]

#case2
depar="ULSAN"
hub="SEOUL"
dest="BUSAN"
roads=[["SEOUL","DAEJEON"],
       ["ULSAN","BUSAN"],
       ["DAEJEON","ULSAN"],
       ["DAEJEON","GWANGJU"],
       ["SEOUL","ULSAN"],
       ["DAEJEON","BUSAN"],
       ["GWANGJU","BUSAN"]
       ]
 
 
 
# http://ejklike.github.io/2018/01/05/bfs-and-dfs.html
 
#두 노드간 경로탐색
 
 # 하 시발,,, nhn자바로 하네? 나 파이썬으로 코테준비하는데?! 시발?! 
node={}
for v1,v2 in roads:
    node[v1]=node.get(v1, [])+[v2]
print(node)
 
def search(node,depar,dest):
    queue=[(depar,[depar])]
 
    result=[]
    while queue:
#         print(queue)
        n,path=queue.pop(0) #이렇게 쌍으로 저장하는거 좀 익숙해지자!! 
        if n==dest :
            result.append(path)
        else:
            for m in node[n]:
#             for m in list(set(node[n])-set(path)):
                queue.append((m,path+[m]))
    return result
 
print(len(search(node, depar,dest)))
answer=search(node, depar, dest)
cnt=0
for a in answer:
    if hub in a:
        cnt+=1
print(cnt)

    


# depar    hub    dest    roads    result
# "SEOUL"    "DAEGU"    "YEOSU"    [["ULSAN","BUSAN"],["DAEJEON","ULSAN"],["DAEJEON","GWANGJU"],["SEOUL","DAEJEON"],["SEOUL","ULSAN"],["DAEJEON","DAEGU"],["GWANGJU","BUSAN"],["DAEGU","GWANGJU"],["DAEGU","BUSAN"],["ULSAN","DAEGU"],["GWANGJU","YEOSU"],["BUSAN","YEOSU"]]    9
# "ULSAN"    "SEOUL"    "BUSAN"    [["SEOUL","DAEJEON"],["ULSAN","BUSAN"],["DAEJEON","ULSAN"],["DAEJEON","GWANGJU"],["SEOUL","ULSAN"],["DAEJEON","BUSAN"],["GWANGJU","BUSAN"]]    0