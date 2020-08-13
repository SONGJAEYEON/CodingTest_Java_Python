from itertools import product

for i in product([1,2,3],'ab'):
    print(i,end=" ")