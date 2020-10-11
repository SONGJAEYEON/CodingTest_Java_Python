#nhn문제1
# https://recruit.nhn.com/pdf/%ED%94%84%EB%A6%AC%ED%85%8C%EC%8A%A4%ED%8A%B8_1%EC%B0%A8_%EA%B8%B0%EC%B6%9C%EB%AC%B8%EC%A0%9C.pdf
# https://juhee-maeng.tistory.com/133
#영역의 개수와 각 영역의 크기를 오름차순으로 출력하ㅔㅅ요

#데이터 인풋을 어떻게 하지?
import sys
input = lambda: sys.stdin.readline().rstrip()
n=int(input())
print(n)
a = [list(map(int, input().split(' '))) for _ in range(6)]
print(a)

# a,b=map(int,input().split(' '))
# print(a," ",b)
