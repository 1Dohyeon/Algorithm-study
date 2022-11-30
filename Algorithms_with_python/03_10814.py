N=int(input())
p=[]

for i in range(N):
    age,name=map(str,input().split())
    age=int(age)
    p.append((age,name))    # 2차원 배열로 만들어서 푼다. 

p.sort(key=lambda p:p[0])  # (age, name)에서 age만 비교 후 정렬


for i in range(N):
    print(p[i][0],p[i][1])

# 'key=lambda p:p[0]'는 2차원 배열p의 여러 변수들 중 0열에 있는 변수들만 정렬한다.
# sort함수에서 key를 통해 정렬 기준을 정할 수 있다는 것을 새롭게 알게되었다. (key=len일 경우는 길이에 따라 정렬)
