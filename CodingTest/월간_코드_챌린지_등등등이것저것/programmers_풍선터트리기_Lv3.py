a=[-16,27,65,-2,58,-92,-71,-68,-61,-33]
cnt=0
for i in range(len(a)):
    me=a[i]
    prefix_min=min(a[:i+1])
    suffix_min=min(a[i+1:])
print(cnt)    
    
