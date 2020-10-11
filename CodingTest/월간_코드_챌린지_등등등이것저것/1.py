N=14

def numeral_system(number, base):
    NOTATION = '0123456789ABCDEF'
    q, r = divmod(number, base)
    n = NOTATION[r]
    return numeral_system(q, base) + n if q else n

answer=[0,0]
for i in range(2,10):
    total=1
    convertNumber=numeral_system(N,i)
    for s in convertNumber:
        total*=int(s)
    if answer[1]<=total:
        answer=[i,total]
print(answer)        



# n=45
# NOTATION = '0123456789ABCDEF'
# # n    result
# # 45    7
# # 125    229
# def numeral_system(number, base):
#     q, r = divmod(number, base)
#     n = NOTATION[r]
#     return numeral_system(q, base) + n if q else n
#  
# three=list(numeral_system(n, 3))
# answer=0
# for i in range(len(three)):
#     answer+=((3**i)*int(three[i]))
# print(answer)




