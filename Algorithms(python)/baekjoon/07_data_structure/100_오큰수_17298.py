import sys

n=int(sys.stdin.readline())
a=list(map(int, sys.stdin.readline().split()))
stack=[]   
nge=[-1]*n  # 수열의 마지막 수는 -1로 고정, 오큰수가 없을 때는 -1이기 때문에 nge의 기본값은 -1로 지정한다.
stack.append(0)

for i in range(1,len(a)):
    while stack and a[stack[-1]]<a[i]:  # a의 i번째 원소가 스택에 top에 있는 수를 인덱스로 두는
        nge[stack.pop()]=a[i]   # 배열 a보다 크다면 stack의 top을 인덱스로 두는 nge의 원소에 a[i]를 담는다.
    stack.append(i)  

print(*nge) # *를 이용하여 리스트 형식을 한 칸씩 띄워서 출력한다.




''' 두 개의 for문으로 수열을 돌기 때문에 시간 초과에 걸린다.
import sys

n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))  
nge=[]

for i in range(n):
    for j in range(i+1,n):
        if a[j]>a[i]:   
            nge.append(a[j])   
            break               
    else:  
        nge.append(-1)  

print(*nge) 
'''