T = int(input())
for test_case in range(1, T + 1):
    a,b=map(int,input().split())
    a_list=[input() for i in range(a)]
    b_list=[input() for i in range(b)]
    #공통으로 들어있는 단어의 개수!
    answer=0
    for a_word in a_list: #이것도 람다로 조져도될거같은데 흠 그냥 하쟝
        if a_word in b_list:
            answer+=1
    print("#%d %d" %(test_case,answer))
    