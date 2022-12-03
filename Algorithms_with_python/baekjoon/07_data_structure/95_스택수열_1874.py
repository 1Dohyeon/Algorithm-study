n=int(input())
stack=[]
result=[]
cnt=1
bool=True

for i in range(n):
    num=int(input())

    while cnt<=num: # 스택 배열에 담을 cnt를 1부터 늘려가며 num보다 커지기 전까지 반복
        stack.append(cnt)   
        result.append('+')  # 위 상황에서의 문제 조건은 +를 출력하라 했기에 출력할 result배열애 +를 담는다.
        cnt+=1  
    
    if stack[-1]==num:  
        stack.pop() # 스택 배열의 top을 pop해준다.
        result.append('-')  # pop했을 시 문제 조건은 -를 출력하라 했기에 result배열에 -를 담는다

    else:   # stack의 top이 입력받은 수와 다르다는 것은, 스택의 top이 입력받은 수보다 크기 때문에 입력받은 수는
            # stack의 아래쪽에 쌓여있기에 배열을 완성시킬 수 없으므로 bool을 False로 바꿈
        bool=False

if bool==False:
    print('NO') 
else:  
    for i in result:    
        print(i)
        