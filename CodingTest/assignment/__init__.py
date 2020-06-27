from random import *
##1
from numpy.random.mtrand import randint
print("안녕하세요 \\\n기말고사 대체 레포트\n제출합니다.")

##2
# 그래픽 이런거랑 안친합니다~

##3
while True:
    num=int(input("숫자를 입력하시오 . : "))
    if num>0 and num<11:
        break
    else :
        num=int(input("숫자를 다시 입력하시오. : "))

##4
lotto=[]
inputnum=[]
while True:
    ran1=randint(1,5)
    ran2=randint(1,5)
    if ran1!=ran2 :
        break
    else :
        ran1=randint(1,5)
        ran2=randint(1,5)
lotto.append(ran1)
lotto.append(ran2)
num1 = int(input("첫번째 숫자를 입력하세요. "))
num2 = int(input("두번째 숫자를 입력하세요. "))
inputnum.append(num1)
inputnum.append(num2)
print("로또추첨을 시작합니다")
for i in range(len(lotto)):
    if inputnum[i] in lotto:
        lotto.remove(inputnum[i])
print("로또 번호는 ",ran1," , ",ran2,"입니다")
print("입력하신 로또 번호는 ",num1," , ",num2,"이고 결과는 . . . . .")
if len(lotto)==0:
    print("1등입니다")
elif len(lotto)==1:
    print("2등입니다")
else :
    print("꽝입니다") 

##5
student1 ={"학번": 1000,"이름":"나연","학과":"물리학과"}
student2 ={"학번": 1001,"이름":"지효","학과":"수학과"}
student3 ={"학번": 1002,"이름":"정연","학과":"화학과"}
student4 ={"학번": 1003,"이름":"미나","학과":"수학과"}
student5 ={"학번": 1004,"이름":"사나","학과":"수학과"}
student6 ={"학번": 1005,"이름":"쯔위","학과":"철학과"}
student7 ={"학번": 1006,"이름":"다현","학과":"수학과"}
student8 ={"학번": 1007,"이름":"채영","학과":"물리학과"}
student9 ={"학번": 1008,"이름":"모모","학과":"물리학과"}
student_list=[]
student_list.append(student1)
student_list.append(student2)
student_list.append(student3)
student_list.append(student4)
student_list.append(student5)
student_list.append(student6)
student_list.append(student7)
student_list.append(student8)
student_list.append(student9)

# 1001~1006번 사이에 수학과가 몇멍있는지 출력하는 프로그램
cnt=0
for i in range(1,6):
    if student_list[i]["학과"]=="수학과":
        cnt+=1
print("1001~1006 사이에 수학과는 4명입니다")


##6 
# 그래픽 이런거랑 안친합니다~

##7
 
# 첨부되어있는 score.csv파일을 불러와서 성적을 검색하여 이름을 출력하는 프로그램을 만들고자한다
# 검색할 과목을 입력한다
import csv
data=[]
#csv를 읽어오는 부분
f=open('score.csv','r')
rdr=csv.reader(f)
for line in rdr:
    data.append(line)
f.close()
header = data[0]
data.remove(header)
 
#과목과 성적을 입력하는 부분
subject=input("어떤 과목 성적을 체크하시겠습니까?")
score =input("몇 점 이상을 출력하시겠습니까?")
 
#과목 인덱스를 찾는 부분
checkboxindex = 0 
for i in range(len(header)):
    if header[i]==subject:# 과목 인덱스를 찾는부분
        checkboxindex=i
print(checkboxindex)
         
#과목을 기반으로 입력된 성적이상의 학생 이름을 추출하는 부분
print(subject+" 과목의 성적이  "+score+"점 이상인 학생들은")
for i in range(len(data)):
    if data[i][checkboxindex]>=score:
        print(data[i][0])
print("입니다")
 
 


