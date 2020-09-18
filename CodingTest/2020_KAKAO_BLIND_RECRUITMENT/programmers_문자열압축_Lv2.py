# s    result
# "aabbaccc"    7
# "ababcdcdababcdcd"    9
# "abcabcdede"    8
# "abcabcabcabcdededededede"    14
# "xababcdcdababcdcd"    17
s="xababcdcdababcdcd"
answer=s
minLen=len(s)

#문자열을 1~len(s)/2개씩 각 단위만큼 잘러서 압축
for unit in range(1,len(s)//2+1):
    tempAnswer=""
    temp=s[:unit]
    print(temp)
    cnt=1
    for i in range(unit,len(s),unit):
        if temp==s[i:i+unit]:
            cnt+=1
        else:
            if cnt==1:
                tempAnswer+=temp
            else:
                tempAnswer+=str(cnt)+temp
        