n,k=map(int,input().split())
coins=[]

for _ in range(n):
    coins.append(int(input()))

cnt=0
for i in range(n-1,-1,-1):
    cnt+=k//coins[i]
    k%=coins[i]
    if k==0:
        print(cnt)
        break

