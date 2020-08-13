import math
def solution(progresses, speeds):
    result=[]
    for i in range(len(progresses)):
        result.append(math.ceil((100-progresses[i])/speeds[i]))
    answer=[]
    maxValue=result[0]
    count=1
    for i in range(1,len(result)):
        if maxValue >= result[i]:
            count+=1
        else:
            answer.append(count)
            maxValue=result[i]
            count=1
        if i==len(result)-1:
            answer.append(count)
    return answer