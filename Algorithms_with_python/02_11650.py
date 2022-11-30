# 2차원 배열에 append를 이용하여 변수를 담는 방법을 처음 알게해준 문제이다.
# 1차원 배열에만 append를 이용하는 문제만 접하였기에 이 문제가 기억에 남는다.

n=int(input())
arr=[]

for i in range(n):
    a,b=map(int,input().split())
    arr.append((a,b))   # 2차원 리스트에 변수 담기

arr.sort()  # 2차원 리스트도 sort를 이용해 정렬할 수 있다.

for i in range(n):
    print(arr[i][0],arr[i][1])  # 원래 행에 상수가 남고 변수는 열에 담긴다고 생각했는데 행에 변수가 담기고 열이 기준인 것 같다.