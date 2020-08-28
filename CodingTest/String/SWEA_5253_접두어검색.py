#접두어랑 부분문자열은 다른거야!!! 부분문자열인데 접두어로 생각해서 풀라그랬내? 
#그룹 A와 : 주어질 때 B에 속한 문자열 중 A의 접두어인 문자열의 개수를 알아내는 프로그램을 만드시오 
# A=["able",'abl','abroad']
# B=['ab','abo','a']
#제한시간 초과가 떠버렸네?
T = int(input())
whole_pre_word=[]
for test_case in range(1, T + 1):
    a,b=map(int,input().split())
    A=[input() for i in range(a)]
    print(A)
    B=[input() for i in range(b)]
    print(B)
    for word in list(map(lambda x :[x[:i+1] for i in range(len(x))],A)):
        whole_pre_word+=word #람다식으로 못줄이나,,?
    whole_pre_word=list(set(whole_pre_word))
    print("#%d %d" %(test_case,len(list(filter(lambda x: x in whole_pre_word,B)))))