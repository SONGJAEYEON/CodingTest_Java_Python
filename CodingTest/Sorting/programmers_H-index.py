def solution(citations):
    answer = 0
    maxValue=max(citations)
    for i in range(maxValue,0,-1):
        citations.append(i)
        citations.sort(key=None, reverse=True)
        flag=citations.index(i)
        if len(citations[:flag])>=i and len(citations[flag+1:])<=i:
            answer=i
            break
        else : 
            citations.remove(i)
    return answer