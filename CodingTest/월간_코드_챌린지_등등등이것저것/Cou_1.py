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

#십진수가 주어지면 주어진 십진수를 2부터 9까지의 진수로 변환하고나서 애를 문자열 뒤집듯 뒤집었을때의 숫자를 모두 곱했을때 나오는 수가 가장 클때 그때의 [진법,곱한 결과] 를 리턴
#만약 수가 같으면 더 큰 진법이 답이 될수있도록 구현