from math import sqrt
def solution(b, y):
    return [int(((b+4)/2+sqrt(((b+4)/2)**2-4*(b+y)))/2),int(((b+4)/2-sqrt(((b+4)/2)**2-4*(b+y)))/2)]