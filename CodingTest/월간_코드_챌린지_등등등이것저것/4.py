s="baby"


def solution(s):
    prestr=list(filter(lambda x: len(x)>1,[s[i:j] for j in range(1,len(s)+1) for i in range(len(s))]))
    preStr=list(filter(lambda x:len(set(list(x)))!=1,prestr))
    # print(preStr)
    beauty=0
    if len(preStr)==0:
        return 0
    else:
        for substr in preStr:
            chk=True
            startidx=0
            lastidx=len(substr)-1
            while chk:
                if substr[startidx]!=substr[lastidx]:
                    beauty+=(lastidx-startidx)
                    chk=False
                else:#두 글자가 같다면
                    if lastidx-1 != startidx: #시작인덱스와 라스트인덱스가 맞닿아 있지않다면
                        lastidx-=1
                    else:# 맞닿아있다면 스타트를 +1하고 라스트는 다시 맨 뒤로 보내자!!
                        if startidx+1==len(substr)-2:
                            chk=False#하지만 스타트+1이 부분문자열의 길이-2와 같다면 그냥 브레이크
                        else:
                            startidx+=1
                            lastidx-=len(substr)-1
    return beauty
print(solution(s))