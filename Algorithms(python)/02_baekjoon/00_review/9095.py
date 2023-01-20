t=int(input())

d=[0 for i in range(13)]
d[1]=1  # 1
d[2]=2  # 1 1 or 2
d[3]=4  # 1 1 1 or 1 2 or 2 1 or 3
d[4]=7  # 1 1 1 1 or 1 1 2 or 1 2 1 or 2 1 1 or 2 2 or 1 3 or 3 1 

for i in range(5,11):
    d[i]=d[i-1]+d[i-2]+d[i-3]
    # 1, 2, 3 으로만 i를 만들 때 i-1에서 1을 더하는 경우의 수, i-2에서 2를 더하는 경우의 수, i-3에서 3을 더하는 경우의 수밖에 없으므로
    # i-1, i-2, i-3의 경우의 수의 합과 같다.
for _ in range(t):
        n=int(input())
        print(d[n])
    