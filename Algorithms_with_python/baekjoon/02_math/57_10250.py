T=int(input())

for i in range(T):
    H,W,N=map(int,input().split())  # 호텔의 층 수, 방 수, 손님 순서
    w=N//H+1
    h=N%H
    if N%H==0:  # N%H=0일때, 층수는 꼭대기 층이고, 호수는 다시 1층으로 안넘어갔으므로 N/H의 몫이랑 같다
        h=H
        w=N//H
    
    print(h*100+w)
    
