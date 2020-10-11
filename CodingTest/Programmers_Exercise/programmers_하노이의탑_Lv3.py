
# https://shoark7.github.io/programming/algorithm/tower-of-hanoi



def hanoi(num, start, to, mid, answer):
    #종료조건
    if num == 1:
        return answer.append([start, to])
    #﻿1번 기둥에 있는 n개의 원반 중 n-1개를 2번 기둥으로 옮깁니다.(3번 기둥을 거쳐감)
    hanoi(num-1, start, mid, to, answer)
    answer.append([start, to])
    #﻿2번 기둥에 있는 n-1개의 원반을 다시 3번 기둥으로 옮깁니다.(1번 기둥을 거쳐감)
    hanoi(num-1, mid, to, start, answer)
def solution(n):
    answer = []
    hanoi(n, 1, 3, 2, answer)
    return answer
  
print(solution(3))

# MSG_FORMAT = "{}번 원반을 {}에서 {}로 이동" #와우,,,,! 개쩌네,,?! 
# n=4
# answer=[]
# def move(N, start, to):
#     return answer.append([start,to])
# #     print(MSG_FORMAT.format(N, start, to))
#      
# def hanoi(N, start, to, via):
#     if N == 1:
#         move(1, start, to)
#     else:
#         hanoi(N-1, start, via, to)
#         move(N, start, to)
#         hanoi(N-1, via, to, start)
#          
# hanoi(n, 1, 3, 2)
# print(answer)









