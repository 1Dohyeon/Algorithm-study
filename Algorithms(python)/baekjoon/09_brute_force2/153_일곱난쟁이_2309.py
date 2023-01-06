import sys

cm=[]

for i in range(9):
    cm.append(int(sys.stdin.readline()))

for i in range(len(cm)-1):
    for j in range(i+1,len(cm)):
        a=cm[i]
        b=cm[j]
        cm[i]=0
        cm[j]=0
        if sum(cm)==100:
            break
        else:
            cm[i]=a
            cm[j]=b

cm.remove(0)
cm.remove(0)
cm.sort()

for r in cm:
    print(r)


        
