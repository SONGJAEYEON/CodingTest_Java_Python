def solution(bridge_length, weight, truck_weights):
    count=1
    group=[]
    plus=truck_weights[0]
    if len(truck_weights)==1:
        group=[1]
    else:
        for i in range(1,len(truck_weights)):
            if plus+truck_weights[i]<=weight:
                count+=1
                plus+=truck_weights[i]
            else:
                group.append(count)
                plus=truck_weights[i]
                count=1
            if i==len(truck_weights)-1:
                group.append(count)
    answer=1
    answer+=(sum(group)-len(group))
    answer+=(bridge_length*len(group))
    return answer