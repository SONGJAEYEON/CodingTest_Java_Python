# arr=[3,6,7,2,5,4,1]
arr=[1,2,3]
n=len(arr)
for i in range(1<<n): #1<<n:부분집합의 개수
    print(i,":",end="")
    for j in range(n):#원소의 수만큼 비트를 비교함
        if i&(1<<j):#i의j번째비트가 1이면 j번째 원소가 출력
            print(arr[j],end=" ")
    print()
#부분집합만들기 코드를 미리 만들어놔야겠는걸~

# https://withcoding.com/77
#여기 블로그에있는 집합관련 메소드들 숙지하자!! 상당히 유용하게 쓰일거같습니다!!!