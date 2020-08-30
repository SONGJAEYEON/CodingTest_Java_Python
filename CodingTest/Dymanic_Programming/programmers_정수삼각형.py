# https://wwlee94.github.io/category/algorithm/dp/school-road/
triangle=[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

value=[[0 for j in range(len(triangle[i]))] for i in range(len(triangle))]
value[0][0]=triangle[0][0]
print(value)

#enumerate랑 range중에서 뭐가 더 빨라여?
for x in range(len(triangle)-1):
    for y in range(len(triangle[x])):
        value[x+1][y]=max(value[x+1][y],value[x][y]+triangle[x+1][y])
        value[x+1][y+1]=max(value[x+1][y+1],value[x][y]+triangle[x+1][y+1])
        print(value[x])
    print()
print(max(value[-1]))

#]solution = lambda t, l = []: max(l) if not t else solution(t[1:], [max(x,y)+z for x,y,z in zip([0]+l, l+[0], t[0])])
#?????????????//
#진짜 물음표백만개다,,,,