N=int(input())
count=0

while N>=0: # N=0일때, 0을 출력해야하므로 0도 범위에 포함
    if N%5==0:  
        count+=N//5
        print(count)
        break

    N-=3
    count+=1

else:   
    print(-1)
