#1
# P    N    answer
# PM 01:00:00    10    13:00:10
# PM 11:59:59    1    00:00:00
# 입출력 예 설명



# "PM 11:59:59"
P="AM 12:01:00"
#"PM 11:59:59"
N=1


#라이브러리 미사용


#라이브러리 사용 
# from datetime import datetime,timedelta

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