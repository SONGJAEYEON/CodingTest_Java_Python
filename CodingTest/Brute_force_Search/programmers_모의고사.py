def solution(answers):
    size=len(answers)
    answer=[0,0,0]
    stu1=[1,2,3,4,5]*2000
    stu1=stu1[:size]
    stu2=[2,1,2,3,2,4,2,5]*1250
    stu2=stu2[:size]
    stu3=[3,3,1,1,2,2,4,4,5,5]*1000 # 총 10개니까 1000번 ^^
    stu3=stu3[:size]
    for i in range(size):
        if answers[i]==stu1[i]:
            answer[0]+=1
        if answers[i]==stu2[i]:
            answer[1]+=1
        if answers[i]==stu3[i]:
            answer[2]+=1
    result=[]
    for i in range(3):
        if max(answer)==answer[i]:
            result.append(i+1)
    return result