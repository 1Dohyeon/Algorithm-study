# 유클리드 호제법

'''최대공약수(gcd)는 두 수 a,b가 있고, a를 b로 나눈 나머지를 r이라고 했을 때 gcd(a,b)=gcd(b,r)이다.
r=0이 될 때, 그 때의 b가 최대 공약수이다.

ex) a=24,b=16일 때 r=24%16=8, gcd(a,b)=gcd(b,r)이기 때문에 24, 16의 gcd = 16, 8의 gcd   ->
    r=16%8=0, 이때 b=8이므로 gcd = 8.  

def gcd(a,b):   
    while b!=0:
        r=a%b
        a=b
        b=r
    return a 

최소공배수(lcm)는 두 수 a,b가 있고 a,b의 gcd를 g라고 했을 때 lcm=g*(a/g)*(b/g)=(a*b)/g이다.
''' 

a,b=map(int,input().split())
x,y=a,b

while y!=0:
    r=x%y
    x=y
    y=r

print(x)    # 최대공약수

l=(a*b)/x
print(int(l))   # 최소공배수