def solution(priorities, location):
    size=len(priorities)
    result=[0 for _ in range(size)]
    result[location]="here"
    order=[]
    while(True):
        if len(order)==size:
            break
        maxValue=max(priorities)
        nowValue=priorities.pop(0)
        nowPosition=result.pop(0)
        if(maxValue>nowValue):
            priorities.append(nowValue)
            result.append(nowPosition)
        else:
            order.append(nowPosition)
    return order.index("here")+1