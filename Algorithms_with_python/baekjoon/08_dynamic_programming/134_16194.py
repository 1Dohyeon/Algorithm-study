import sys

n=int(sys.stdin.readline())
p=[0]+list(map(int,sys.stdin.readline().split()))   
d=[0]*(n+1) 
d[1]=p[1]  

for i in range(2,n+1):
    for j in range(1, i+1):
        if d[i]==0: # d[i]=0이라는 값도 나오므로 d[i]=0일 때 d[i]=d[i-j]+p[j]
            d[i]=d[i-j]+p[j]
        else:
            d[i]=min(d[i],d[i-j]+p[j]) 
print(d[i])                              
                                       
