# people=[40,40,40,40,40]
# #[120,150,40,40,80,40,50,60,200,110,70,50,60,80,90,100] #이게 5만명이하라는거지?
# limit=100
# people.sort(reverse=True)
# print(people)
# heavy,light,save,boat=map(int,[0,len(people)-1,0,0])
# while(save<len(people)):
#     if limit-people[heavy]>=people[light]:
#         save+=2
#         boat+=1
#         heavy+=1
#         light-=1
#     else:
#         save+=1
#         boat+=1
#         heavy+=1   
# print(boat)

#서로다른 3개를 더했을 때 소수가 되는 경우의 개수
# [1,2,3,4]    1 
# [1,2,7,6,4]    4
# 입출력 예 #1
# [1,2,4]를 이용해서 7을 만들 수 있습니다.
# 
# 입출력 예 #2
# [1,2,4]를 이용해서 7을 만들 수 있습니다.
# [1,4,6]을 이용해서 11을 만들 수 있습니다.
# [2,4,7]을 이용해서 13을 만들 수 있습니다.
# [4,6,7]을 이용해서 17을 만들 수 있습니다.
# 제한사항
# nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
# nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.
#아리스토테네스의 채 찾아야겠네

#jaden case문자열 빨리만드는방법,,!!
# #문자열 S가 주어졌을 때 s를 jadencase로 바꾼 문자ㅕㅇㄹ을 리턴
s="3people unFollowed me"
# S="3people Unfollowed Me"
# #첫 문자가 영문이 아닐때에는 이어지는 영문은 소문자로 씁니다 
# P="3People Unfollowed Me"
s.title()
print(s)
# chk_digit=s.split(" ")
# for i in range(len(chk_digit)):
#     if chk_digit[i][0].isnumeric():
#         new_word=chk_digit[i].replace(chk_digit[i][1],chk_digit[i][1].lower())
#         chk_digit[i]=new_word
# print(" ".join(chk_digit))







