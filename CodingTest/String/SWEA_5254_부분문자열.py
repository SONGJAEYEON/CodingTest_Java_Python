# arr=[3,6,7,2,5,4,1]
str="abac"
arr=list(str)
n=len(arr)
k=5
sub_word=[]
for i in range(1<<n): #1<<n:부분집합의 개수
    for j in range(n):#원소의 수만큼 비트를 비교함
        if i&(1<<j):#i의j번째비트가 1이면 j번째 원소가 출력
            sub_word.append(arr[j])
print(sub_word)