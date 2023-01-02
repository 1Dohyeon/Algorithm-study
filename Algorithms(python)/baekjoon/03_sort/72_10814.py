N=int(input())
p=[]

for i in range(N):
    age,name=map(str,input().split())
    age=int(age)
    p.append((age,name))    # 입력받은 값 중 age는 int타입으로 바꾸고 2차원 배열에 담는다. 

p.sort(key=lambda p:p[0])  # (age, name)에서 age만 비교 후 정렬


for i in range(N):
    print(p[i][0],p[i][1])

