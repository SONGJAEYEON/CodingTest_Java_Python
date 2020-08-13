def solution(jobs):
    jobs.sort(key=lambda x:x[1], reverse=False)
    case_2=getTime(jobs)
    return  case_2

def getTime(jobs):
    size=len(jobs)
    totalValue=0
    requestTime=[0 for _ in range(size)]
    for i in range(size):
        totalValue+=jobs[i][1]
        requestTime[i]=totalValue-jobs[i][0]
    return sum(requestTime)//size