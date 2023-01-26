t=int(input())

for _ in range(t):
    vps=list(input())
    stack=[]

    for i in vps:
        if i=='(':
            stack.append(i)
        elif i==')':
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if len(stack)==0:
            print('YES')
        else:
            print('NO')

'''
t=int(input())

for _ in range(t):
    vps=list(input())
    stack=[]

    for i in vps:
        if i=='(':
            stack.append(i)
        elif i==')' and stack:
            stack.pop()
        elif i==')' and len(stack)==0:
            print('NO')
            break
    else:
        if len(stack)==0:
            print('YES')
        else:
            print('NO')
'''