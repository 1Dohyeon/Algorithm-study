case=int(input())

for i in range(case):
    n=list(map(int,input().split()))
    avg=sum(n[1:])/n[0]
    count=0

    for j in range(1,n[0]+1):   
        if(n[j]>avg):
            count+=1

    result=count/n[0]*100
    
    print(f'{result:.3f}%') #
   
