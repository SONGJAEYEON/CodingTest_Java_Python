#https://eda-ai-lab.tistory.com/490
#https://jisun-rea.tistory.com/entry/python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Level2-JadenCase-%EB%AC%B8%EC%9E%90%EC%97%B4-%EB%A7%8C%EB%93%A4%EA%B8%B0?category=765195

s="3people unFollowed me"
l=s.lower().split(" ")
for i,w in enumerate(l):
    if len(w)<2:
        l[i]=w.upper()+" "
    else:
        l[i]=w[0].upper()+w[1:]+" "
print("".join(l)[:-1])

chkList=s.lower().split(" ")
for i,w in enumerate(chkList):
    chkList[i]=w.capitalize()+" "
print("".join(chkList)[:-1])