
##333333333333333333333333333333333333333333

# k    score    result
# 3    [24,22,20,10,5,3,2,1]    3
# 2    [1300000000,700000000,668239490,618239490,568239490,568239486,518239486,157658638,157658634,100000000,100]    4


# k=3
# score=[24,22,20,10,5,3,2,1]
# #[1300000000,700000000,668239490,618239490,568239490,568239486,518239486,157658638,157658634,100000000,100]
# total=len(score)
# dic={}
# for i in range(len(score)-1):
#     value=abs(score[i]-score[i+1])
#     if value in dic:
#         dic[value][0]+=1
#         dic[value][1].update([i,i+1])
#     else:
#         dic[value]=[1,set([i,i+1])]
# print(dic)
# rem=set()
# for l in dic.values():
#     if l[0]>=k:
#         rem.update(l[1])
# print(total-len(rem))
# differ=[0 for i in range(len(score)-1)]
# for i in range(len(differ)):
#     differ[i]=[i,i+1,abs(score[i]-score[i+1])]
# print(differ)
