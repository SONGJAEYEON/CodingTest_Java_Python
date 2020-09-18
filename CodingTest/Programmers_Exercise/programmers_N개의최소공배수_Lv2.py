arr=[2,6,8,14]
#로직 잘못짰다 다시생각하자!!
    
    
n=4
ans=[1,1,2]

for i in range(3,n+1):
    ans.append(ans[i-1]+ans[i-2])
print(ans)
print(ans[n])