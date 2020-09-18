n=4
# https://leedakyeong.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-2-x-n-%ED%83%80%EC%9D%BC%EB%A7%81-in-python-%ED%8C%8C%EC%9D%B4%EC%8D%AC
#가로의 길이 n은 6000이하의 자연수 입니다 
tile=[0 for _ in range(n+1)]
tile[1]=1
tile[2]=2
for i in range(3,n+1):
    tile[i]=tile[i-1]+tile[i-2]
print(tile[-1])


# def solution(n):
#     f = []
#     f.append(1)
#     f.append(2)
#     for i in range(2, n):
#         f.append((f[-1] + f[-2])% 1000000007) # 처음에 리스트를 초기화하지않고 하는방법도있구만,,!!
#     return f[-1]
# 
# 
# 출처: https://leedakyeong.tistory.com/entry/프로그래머스-2-x-n-타일링-in-python-파이썬 [슈퍼짱짱]

#졸라 신기한 피보나치 수 구하는 방법 
# n=8
# a,b=1
# for i in range(n):
#     (a,b)=(b,a+b)
# print(a%1000000007)