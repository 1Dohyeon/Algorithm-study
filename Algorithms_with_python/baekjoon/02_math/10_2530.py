A,B,C=map(int,input().split())
D=int(input())

C1=(C+D)%60 #최종 초
B1=(C+D)//60
B2=(B+B1)%60 #최종 분
A1=(B+B1)//60
A2=(A+A1)%24 #최종 시각

print(A2,B2,C1)

