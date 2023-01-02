import sys

stack1=list(sys.stdin.readline()) 
stack1.pop()
stack2=[]
n=int(sys.stdin.readline())

for i in range(n):
    comd=sys.stdin.readline().split()   # comd[0]은 명령어, comd[1]은 추가할 문자이다.    

    if comd[0]=='L' and stack1: # 명령어가 L이고 stack1이 존재할 경우
        stack2.append(stack1.pop())

    # 왜 stack==True라고 적으면 에러가 나는지 모르겠음..

    elif comd[0]=='D' and stack2:
        stack1.append(stack2.pop())

    elif comd[0]=='B' and stack1:   
        stack1.pop()

    elif comd[0]=='P':
        stack1.append(comd[1])


print("".join(stack1+list(reversed(stack2))))   # list, reversed를 통해 stack2를 뒤집고 list타입으로 바꿈. 
                                                # "".join() 함수를 통해 stack1과 stack2를 간격 없이 문자로 출력. 


