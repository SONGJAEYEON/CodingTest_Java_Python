# https://it-garden.tistory.com/403?category=845076
def gcd(a,b): #최대공약수
    if b==0:
        return a
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)
x=54
y=20

#최대공약수 GCD
print(gcd(x,y))

#최소공배수 LCM
print(int(x*y)/gcd(x,y))