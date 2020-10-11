#정규표현식을 공부하자!!

def solution(files):
    import re
    #1. 정규식을 사용해서 숫자를 골라낸다.
    temp=[re.split(r"([0-9]+)",s) for s in files]
    print(temp)
    
    #2. 숫자는 숫자대로 글자는 글자대로 해서정렬한다.
    sort=sorted(temp,key=lambda x:(x[0].lower(),int(x[1])))
    print(sort)
    
    #3. 문자열형태로 다시 합쳐서 출력
    return ["".join(s) for s in sort]


# 
# ###########1번
# # 예1    "...!@BaT#*..y.abcdefghijklm"    "bat.y.abcdefghi"
# # 예2    "z-+.^."    "z--"
# # 예3    "=.="    "aaa"
# # 예4    "123_.def"    "123_.def"
# # 예5    "abcdefghijklmn.p"    "abcdefghijklmn"
# # 입출력 예에 대한 설명
# import re
# 
# # 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
# new_id= ""
# new_id=new_id.lower()
# # print(new_id)
# 
# # 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
# # new_id=re.sub('[=+,#/\?:^$@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', new_id)
# new_id=re.sub('[=+,#/\?:^$@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', new_id)
# ~!@#$%^&*=+
# [=+,#/\?:^$@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>/{/}`\'…》]
# # print(new_id)
# # 3. 정규표현식 예제
# # 
# #    ```python
# #    # 이메일
# #    ^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*.[a-zA-Z]{2,3}$
# # 
# #    # 비밀번호 (특수문자 / 문자 / 숫자 포함 형태의 8~15자리 이내)
# #    ^.*(?=^.{8,15}$)(?=.*\d)(?=.*[a-zA-Z])(?=.*[!@#$%^&+=]).*$
# # 
# #    # 비밀번호 ( 숫자, 문자를 포함하는 6~12자리 이내)
# #    ^[A-Za-z0-9]{6,12}$
# # 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
# # new_id=re.sub('..+', '.',new_id)
# # print(new_id)
# while ".." in new_id:
#     new_id=new_id.replace("..",".")
# print(new_id)
# # 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
# 
# #앞
# new_id=(new_id[1:] if new_id[0]=="."  else new_id)
# # print(new_id)
# #뒤
# new_id=(new_id[:len(new_id)-1] if len(new_id)!=0 and new_id[-1]=="."  else new_id)
# 
# # 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
# new_id=("a" if len(new_id)==0  else new_id)
# 
# # 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
# new_id=(new_id[:15] if len(new_id)>=16 else new_id)
# 
# #      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
# while ".." in new_id:
#     new_id=new_id.replace("..",".")
# # print(new_id)
# #앞
# new_id=(new_id[1:] if new_id[0]=="."  else new_id)
# #뒤
# new_id=(new_id[:len(new_id)-1] if new_id[-1]=="."  else new_id)
# # 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
# new_id=(new_id+(new_id[-1]*(3-len(new_id))) if len(new_id)<3 else new_id)
# 
# print(new_id)
# print(len(new_id))

























































# orders    course    result
# ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]    [2,3,4]    ["AC", "ACDE", "BCFG", "CDE"]
# ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]    [2,3,5]    ["ACD", "AD", "ADE", "CD", "XYZ"]
# ["XYZ", "XWY", "WXA"]    [2,3,4]    ["WX", "XY"]

orders=["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course=[2,3,5]
result=["ACD", "AD", "ADE", "CD", "XYZ"]



# from itertools import combinations
# def solution(orders, course):
#     orders_str=sorted(list(set(list("".join(orders)))))
#     numOfMenu=len(orders_str)
#     answer=[]
#     for case in course:
#         cntList=[[] for i in range(len(orders))]
#         #일단 단품 두개붙어있는거 먼저 해보자!!
#         # all=list()
#         # all.extend([k for k in combinations([j for j in range(numOfMenu)], case)])
# 
#         for case in [k for k in combinations([j for j in range(numOfMenu)], case)]:
#             temp=list(map(lambda idx:orders_str[idx],case))
#             # temp=[]
#             # for idx in case:
#             #     temp.extend([orders_str[idx]])
#             cnt=0
#             for order in orders:
#                 if set(temp).issubset(order):  
#                     cnt+=1
#             cntList[cnt].append("".join(temp))
#         for i in range(len(cntList)-1,0,-1):
#             if i!=1 and len(cntList[i])>0:
#                 answer.extend(cntList[i])
#                 break
#     answer.sort()
#     return answer


# 
# from itertools import combinations
# 
# 
# #orders에 있는 모든 글자를 다 합쳐서 리스트로만든다음에 셋으로바꿔 
# orders_str=sorted(list(set(list("".join(orders)))))
# # print(orders_str)
# numOfMenu=len(orders_str)
# # print(numOfMenu)
# 
# answer=[]
# # for case in course:
# #     all.extend([set(k) for k in combinations([j for j in range(numOfMenu)], case)])
# # print(all)
# for case in course:
#     #일단 단품 두개붙어있는거 먼저 해보자!!
#     all=list()
#     all.extend([k for k in combinations([j for j in range(numOfMenu)], case)])
# #     print(all)
# #     print(len(all))
#     menuDic={} #딕셔너리말고 힙으로 못하나,,?
#     for case in all:
#     #     print(case[0]," ",case[1])
#         temp=[]
#         for idx in case:
#             temp.extend([orders_str[idx]])
#         for order in orders:
#             temp_str="".join(temp)
#             if set(temp).issubset(list(order)):         
#                 if temp_str in menuDic:
#                     menuDic[temp_str]+=1
#                 else:
#                     menuDic[temp_str]=1
# #     print(menuDic)
# #     if len(menuDic)==1:
# #         #최소 두명이상의 손님에게서 주문된 구성만 코스요리 후보에 들어가므로
# #         #요리3개로 구성된 코스요리는 새로 추가하지않습니다. 
# #         continue
#     if not menuDic:
#         break
#     sortedList=sorted(list(menuDic.items()),key=lambda x:-x[1])
#     maxValue=sortedList[0][1]
#     print(maxValue)
#     countDic={}
#     for key,value in sorted(list(menuDic.items()),key=lambda x:-x[1]):
#         if value==maxValue and value!=1:#최소 두명이상의 손님에게서 주문된 구성만 코스요리후보에
#             answer.extend([key])
# answer.sort()
# print(answer)


#13 14 15 시간초과 제발

#     answer.append(sorted(list(menuDic.items()),key=lambda x:-x[1])[0][0])
#     print(answer)
#이 과정이 필요한지 아닌지 잘 모르겠어,, 
# print(orders)
# for i in range(len(orders)):
#     orders[i]="".join(sorted(list(orders[i])))
# print(orders)

        

info=["java backend junior pizza 150",
      "python frontend senior chicken 210",
      "python frontend senior chicken 150",
      "cpp backend senior pizza 260","java backend junior chicken 80",
      "python backend senior chicken 50"]

query=["java and backend and junior and pizza 100",
       "python and frontend and senior and chicken 200"
       ,"cpp and - and senior and pizza 250",
       "- and backend and senior and - 150",
       "- and - and - and chicken 100",
       "- and - and - and - 150"]

result= [1,1,1,1,2,4]
       
# #아 sql을 자바로 구현하라고? 멋지네~
# for sql in query:
#     sql=sql.replace(, new, count)