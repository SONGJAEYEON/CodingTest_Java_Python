
# s    index    result
# "{cpp{java}}{python}"    [0, 4, 9, 10, 11, 18]    [10, 9, 4, 0, 18, 11]
# "ab{}cd{efg{}h}{ij}"    [3, 6, 11, 3, 14, 11]    [2, 13, 10, 2, 17, 10]


s="{cpp{java}}{python}"
idx=[0, 4, 9, 10, 11, 18]

stack=[]
dict={}

for index,value in enumerate(s):
    if value=='{':
        stack.append(index)
    elif value=='}':
        rightidx=stack.pop();
        dict.setdefault(rightidx, index);
        dict.setdefault(index, rightidx);
answer=[ dict.get(i) for i in idx]
print(answer)
 
        