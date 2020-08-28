n=7
#문제를 잘 읽자~~ 
#특히 제한사항을 똑바로 읽자^^
lost=[3,4,5,6]
reserve=[4,5,7]
stack=[]
i=0
while lost:
    popValue=lost.pop()
    if popValue in reserve:
        reserve.remove(popValue)
    else:
        stack.append(popValue)
#스택이 없는애들이야 스택으로 조져보자!!
thanks=0
#전체명수 7명
#수업못듣는애 len(stack)명
#구원받은애 thanks명
cannot=len(stack)
while stack:
    popValue=stack.pop()
    if popValue-1 in reserve:
        reserve.remove(popValue-1)
        thanks+=1
    elif popValue+1 in reserve:
        reserve.remove(popValue+1)
        thanks+=1
print(thanks)
print(n-cannot+thanks)

#     //solution(3, { 2,3 }, { 1 });//2
#     //solution(5, { 3,4 }, { 4,5 });//4
#     //solution(18, { 7,8,11,12 }, { 1,6,8,10 });//17
#     //solution(24, { 12,13,16,17,19,20,21,22 }, { 1,22,16,18,9,10});//19


        
