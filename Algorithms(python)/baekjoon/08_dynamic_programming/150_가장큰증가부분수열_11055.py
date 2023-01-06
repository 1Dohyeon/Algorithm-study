import sys

n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))
d=[0 for i in range(n)]
d[0]=a[0]

for i in range(1,n):
    for j in range(i):
        if a[i]>a[j] and d[i]<d[j]:

# 11053 문제처럼 앞서있는 i가 상대적으로 뒤에 있는 j보다 클경우, 또 d[i]가 d[j]보다 작을 경우여야만 한다.
# 예를 들어 만약 d[i]<d[j]라는 조건이 없을 경우, 또 j=i-3일때 a[i]>a[j]라면 d[i]=d[i-3]의 값을 가지게 된다. 
# 반복문에 의하여 j=i-2 차례가 되었을 경우 그리고 또 a[i]>a[j]일경우, 그 전에 바뀐 값인 d[i-3]이 d[i-2]보다 큼에도 불구하고
# d[i]=d[i-3]이 아닌 d[i]=d[i-2]의 값을 가지게 된다. d[i-3]>d[i-2]이기 때문에 최댓값을 갖지 못하는 것이다.
# 이해가 가질 않는다면 d[i]<d[j]의 조건을 지우고 배열 a[10, 20, 10, 30, 20, 50]를 입력하면 이해가 갈것이다.

            d[i]=d[j]
    d[i]+=a[i]  # 기본적으로 자기 자신의 합을 가진다.
print(max(d))