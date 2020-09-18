
record=["Enter uid1234 Muzi",
         "Enter uid4567 Prodo",
         "Leave uid1234",
         "Enter uid1234 Prodo",
         "Change uid4567 Ryan"]
enter="Muzi님이 들어왔습니다."
leave="Prodo님이 나갔습니다."

result=[]
userID={}
for re in record:
    re_Arr=re.split(" ")
    if re_Arr[0]=="Enter":
        #닉네임을해시테이블에 넣자
        if re_Arr[1] in userID: #유저아이디 테이블에 아이디가 없다면 아이디와 닉네임을 기록한다.
            userID[re_Arr[1]].append(re_Arr[2])
        else:
            userID[re_Arr[1]]=[re_Arr[2]]
        result.append([re_Arr[1],"님이 들어왔습니다."])
    elif re_Arr[0]=="Change":
        #닉네임을 바꾸는거는
        userID[re_Arr[1]].append(re_Arr[2])
    else:
        result.append([re_Arr[1],"님이 나갔습니다."])
# answer=list(map(lambda x,y: y[x[0]][-1],result,userID))
answer=list(map(lambda y: userID[y[0]][-1]+y[1],result))
print(answer)
    
    