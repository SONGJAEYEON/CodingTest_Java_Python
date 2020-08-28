 
words=["dog","dot","cog","lot","log","hot"]
begin="hit"
target="cog"


def transistale(a,b):
    return sum((1 if x!=y else 0) for x,y in zip(a,b))==1
#크으,,, 함수를 이렇게도 만들수있구나 멋지다,,, 
dict={}
dict[begin]=set(filter(lambda x: transistale(x, begin),words))
#이렇게해서 현재 단어랑 하나만 차이나는부분을 찾아서딕셔너리로 만들어주고!!!
print(dict)

for word in words:
    dict[word]=set(filter(lambda x:transistale(x, word),words))
queue=[(begin,0)]
while queue : # 큐가 빌떄까지
    now,level=queue.pop(0)
    if level>len(words): #큐를 다 탐색했음에도 목표단어가 만들어지지않는다면
        return 0
    for w in dict[now]: # 딕셔너리에서 현재 단어를 키로 가지는 리스트를 뽑아보자!!
        if w==target:
            return level+1 # 찾았으면 리턴!!
        else:
            queue.append((w,level+1))
            #현재 키값에서 찾지못했으면 넣고넣고넣고
return 0 # quene에 있는걸 다 썼는데도 못찾았으면0을 리턴!!