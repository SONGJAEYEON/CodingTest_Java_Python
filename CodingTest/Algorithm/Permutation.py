#라이브러리가 훨씬빠름^^
#파이썬 documentation에서 어떻게 구현했는지 나중에 차차 확인해봐욤~

#1. itertools를 이용하여 순열,조합 구현하기
from itertools import permutations

for i in permutations([1,2,3,4],2):
    print(i,end=" ")