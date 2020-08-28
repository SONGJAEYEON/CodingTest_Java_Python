# def solution(numbers):
#     answer = ''
#     numbers=list(map(str,numbers))
#     numbers.sort(key=lambda x:x*3,reverse=True)
#     if sum(list(map(int,numbers)))==0:
#         numbers=list(set(numbers))
#     return "".join(numbers)

numbers=[3,30,34,5,9]
answer="9534330"
#[6,10,2]
#"6210"
numbers=list(map(lambda x:str(x),numbers))
numbers.sort(reverse=True)
print(numbers)
#이거 아까 그리디로 해서 풀어야할거같음,,!!