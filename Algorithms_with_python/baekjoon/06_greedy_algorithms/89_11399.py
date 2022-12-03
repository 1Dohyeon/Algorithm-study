N=int(input())
P=list(map(int,input().split()))
P.sort()

def f(): 
    result=0
    for i in range(N):
        result+=sum(P[0:i+1])
    print(result)

f()
