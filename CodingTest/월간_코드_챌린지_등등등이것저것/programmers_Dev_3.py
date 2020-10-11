#3
# 입출력 예
# votes    k    result
# ["AVANT", "PRIDO", "SONATE", "RAIN", "MONSTER", "GRAND", "SONATE", "AVANT", "SONATE", "RAIN", "MONSTER", "GRAND", "SONATE", "SOULFUL", "AVANT", "SANTA"]    2    "RAIN"
# ["AAD", "AAA", "AAC", "AAB"]    4    "AAB"

votes=["AAD", "AAA", "AAC", "AAB"]
k=4
cnt={}
for v in votes:
    if v in cnt:
        cnt[v]+=1
    else:
        cnt[v]=1
filtered=sorted(cnt.items(),key=lambda x:(-x[1],x[0]),reverse=True)
print(filtered)

cntTop,cntDown,lastPang=0,0,""
for i in range(len(filtered)-1,len(filtered)-1-k,-1):
    cntTop+=filtered[i][1]
print(cntTop)

for i in range(len(filtered)):
    if cntTop<=(cntDown+filtered[i][1]):
        break
    else:
        cntDown+=filtered[i][1]
        lastPang=filtered[i][0]
        print(lastPang," ",cntDown," ",cntTop)
print(lastPang)


    