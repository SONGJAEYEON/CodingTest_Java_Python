#동적계획법
#입력크기가 작은 부분문제들을 해결한 뒤 해당 부분 문제의 해를 활용하여 큰 크기의 부분 문제를 해결하면서 최종적으로 전체문제를 해겨랗는 알고리즘
#상향식 접근법-> 최하위의 대답을 구하고 이를 저장하고 해당 결과값을 이용한 상위문제를 풀어가는방식
#메모제이션 : 프로그램 실행 시 이전에 계산한 값을 저장해 다시 계산하지않도록 하여 전체 실행속도를 향상시키는 기술
#문제를 잘게 쪼갤때 부부ㄴ문제ㅡㄴ 중복되어 재활용됨 

#이 문제 진짜 오늘 꼭 풀고싶어  약간 조이스틱급 까진 아니지만 그래도 약간 그런늭김 ㅎ 이거 두개 하고 레벨테스트하고 집갈까 
#https://muang-kim.tistory.com/208?category=849248
#못풀겠네여,,ㅎ

N=2
number=11
def solution(N, number):
    dp = [[] for _ in range(9)]
    answer = -1
    ## 최솟값이 8보다 큰 경우는 고려하지 않는다. 오오,,, 이렇게 생각을 할 수도 있구나,,, 대다네,,,, 와우,,, 
    for i in range(1, 9):
        ## 숫자를 이어붙이는 경우(5, 55, 555...)
        dp[i].append(int(str(N)*i))
        for j in range(1, i):
            for x1 in dp[j] :
                for x2 in dp[i - j] :
                    ## 각 경우에 대해 사칙연산을 체크
                    dp[i].append(x1 + x2)
                    dp[i].append(x1 - x2)
                    dp[i].append(x1 * x2)
                    ## 나눗셈에서 분모가 0이면 연산이 안되므로
                    if x2 != 0 :
                        dp[i].append(x1 // x2)
        ## 연산을 마친후 정답을 체크
        if number in dp[i] : 
            answer = i
            break
    print(dp)
    return answer
print(solution(N, number))