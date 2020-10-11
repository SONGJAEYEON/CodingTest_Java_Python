#5번이랑 1
# name="ABABAAAAABA"
# #["JAAAAZABZ","AABCEAAAA","AAAAABCD","JAN","JEROEN","BBBAAAB"9,"ABABAAAAABA"11]
# howmanyclick=list(map(lambda a,b:ord(a)-ord(b),list(name),["A" for _ in range(len(name))]))
# filtered=list(map(lambda x: abs(x-26) if x>13 else x,howmanyclick))
# print(filtered)
# chk_A_Idx=[i+1 if filtered[i]!=0 else 0 for i in range(len(filtered))] #코오,,! 이런게 있었구만!!

#탐욕법에서는 뭉탱이로하지말고 차근차근하는게 맞는거같애,,,

#근데 나 이거 조이스틱 너무하기싫어,,,
#https://jisun-rea.tistory.com/entry/python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Level2-%EC%A1%B0%EC%9D%B4%EC%8A%A4%ED%8B%B1-%ED%83%90%EC%9A%95%EB%B2%95Greedy?category=765195

# cnt=0#총 이동횟수
# numof_A=0 #A의 개수
# maxNum_A=0 #연속된A가 가장 길때 그 A의 갯수
# end_A=0#최대 A일때 문자열의 마지막 인덱스
# start_A=0 #최대A일때 문자열의 첫번째인덱스
# left_rignt_cnt=0#좌우로 왔다갔다 하는 횟수 카운트 아 위아래가 아니고? 좌우구나?

#아니야 군말말고 한번 따라쳐보자,,,
#위 아래 조이스틱 계산
# for i,n in enumerate(name):
#     if n=="A":#A개수의 최대값과 그 인덱스 계산
#         numof_A+=1
#         if numof_A>maxNum_A:
#             maxNum_A=numof_A
#             end_A=i
#     else:
#         numof_A=0
# print("end_A ",end_A)
# print("maxNum_A ",maxNum_A)
# start_A=end_A-maxNum_A+1
# print("start_A", start_A)
# standard=(len(name)+1)//2
# print("standard ",standard)
# # if (len(name)+1)//2>start_A: #이렇게 조건을 잡으면 안되나보옴,,,
# #     print((len(name)-maxNum_A-1) +sum(filtered))    
# # else:
# #     print(sum(filtered)+len(name)-1)


