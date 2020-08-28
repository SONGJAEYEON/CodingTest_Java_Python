truck_weights=[10,10,10,10,10,10,10,10,10,10]
#[4,7,5,5,2,2,2,2,2,2]
#[7,4,5,6]
weight=100
bridge_length=100
time=0
q=[0] * bridge_length
s=0
i=0
q = [0]*bridge_length # queue
while q:
    time+=1 #요거때무네
    s-=q.pop(0)
    if i<len(truck_weights):
        if truck_weights[i]+s<=weight:
            s+=truck_weights[i]
            q.append(truck_weights[i])
            i+=1
        else:
            q.append(0)
    else:
        time+=bridge_length-1 #요기서 그냥 빼는거같으넫./
        break
print(time)

    
    