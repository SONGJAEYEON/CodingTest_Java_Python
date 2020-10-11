# n    t    m    p    result
# 2    4    2    1    0111
# 16    16    2    1    02468ACE11111111
# 16    16    2    2    13579BDF01234567
n=2
t=4
m=2
p=1

#재귀함수 이용
def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]


print convert(233, 2)
print convert(233, 8)
print convert(233, 16)
