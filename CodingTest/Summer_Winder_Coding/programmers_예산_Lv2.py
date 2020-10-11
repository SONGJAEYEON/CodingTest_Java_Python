
d=[1,2,3,4,5]
budget=9
d.sort()
cnt=0
for ele in d:
    budget-=ele
    if budget<0:
        break
    else:
        cnt+=1
print(cnt)