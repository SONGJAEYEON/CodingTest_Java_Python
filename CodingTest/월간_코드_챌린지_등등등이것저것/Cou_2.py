###########22222222222222222222

# n    customers    result
# 3    ["10/01 23:20:25 30", "10/01 23:25:50 26", "10/01 23:31:00 05", "10/01 23:33:17 24", "10/01 23:50:25 13", "10/01 23:55:45 20", "10/01 23:59:39 03", "10/02 00:10:00 10"]    4
# 2    ["02/28 23:59:00 03","03/01 00:00:00 02", "03/01 00:05:00 01"]    2
# n=3 #키오스크의 개수
# 
# customer=["10/01 23:20:25 30", "10/01 23:25:50 26", "10/01 23:31:00 05", "10/01 23:33:17 24", "10/01 23:50:25 13", "10/01 23:55:45 20", "10/01 23:59:39 03", "10/02 00:10:00 10"] #고객의 정보가 담긴 배열

#가장 많은 고객과 매칭되는 키오스크는 몇명의 고객과 매칭되는지 계산해서 return 

# from datetime import datetime,timedelta
# timeList=P.split(" ")
# time=datetime.strptime(timeList[1],'%H:%M:%S')
# if timeList[0]=="AM":
#     time=time+timedelta(seconds=N,hours=-12)
# else:
#     time=time+timedelta(seconds=N,hours=36)
# print(str(time)[11:19])
# 
# # if timeList[0]=="AM":
# #     print(str(time)[11:19])
# # else:
# #     strTime=str(time)
# #     print(str(int(strTime[11:13])+12)+strTime[13:19])


#     
# def convert(info):#정보를입력하면
#     infoList=info.split(" ")
#     time=datetime.strptime(" ".join(infoList[:2]),'%m/%d %H:%M:%S')
#     return [time,time+timedelta(minutes=int(infoList[2]))]#종료날짜를 반환하는!
# 
# cnt=[0 for i in range(n)] #매칭에 되면 하나씩 키오스크 카운트를 업 시키자
# endtime=["" for i in range(n)] #엔드타임을 계산하자 
# 
# #초기화
# for i in range(n):
#     endtime[i]=convert(customer[i])[1]
#     cnt[i]+=1
#     print(i+1,"번으로 들어가실게여~ ")
# #운영되고 있지 않은 키오스크가 있다면 
# #일단 얼마나 운영되지 않았는지계산
# #가장 오래 운영되지 않은 키오스크와 매칭
# #만약 시간이 모두 같다면 가장 작은 인덱스를 가지는 키오스크와매칭
# 
# #모든 키오스크가 운영중이라면
# #종료시간이 가장 작은 키오스크와 매칭