from itertools import combinations_with_replacement

for cwr in combinations_with_replacement([1,2,3,4],2):
    print(cwr,end=' ')