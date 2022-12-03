import sys

def sosu_f(x):
    if x==1:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True

while True:
    n=int(sys.stdin.readline())
    if n==0:
        break
    for i in range(3,n+1,2):    # 문제의 범위만큼 지정
                                # 위 범위에 있는 소수는 홀수이고, 홀수+짝수=홀수를 이용하여 2씩 증가시킴 
        if sosu_f(i): 
            if sosu_f(n-i): #  소수 i를 찾고 n-i도 소수인지 확인해야함
                print(n,'=',i,'+',n-i) 
                break   