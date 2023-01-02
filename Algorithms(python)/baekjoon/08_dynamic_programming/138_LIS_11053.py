import sys

n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))

d=[0 for i in range(n)]

for i in range(n):
    for j in range(i):
        if a[i]>a[j] and d[i]<d[j]: # 배열 a에서 i가 j보다 크다면, 증가한다는 의미이고, d[i]<d[j]라면 그 때 i를 기준으로
                                    # 증가하는 수열의 길이가 j보다 작다면, 수열의 길이를 늘리기 위해
            d[i]=d[j]               # d[i]=d[j]라는 값을 가지게 되고
    d[i]+=1                         # 배열 a의 모든 원소는 자기 자신의 크기만큼 길이를 가지고 있으므로 d[i]+=1 
print(max(d))

