# 사용할 수 있는 숫자가 담긴 배열 numbers 타켓넘버 target이 매개변수로 주어질때 만드는방법의 수를 return 하도록

numbers=[1,1,1,1,1]
target=3
up=[0]
for number in numbers:
    down=[]
    for up_element in up:
        down.append(up_element+number)
        down.append(up_element-number)
    up=down
print(up.count(target))
#https://eda-ai-lab.tistory.com/475

