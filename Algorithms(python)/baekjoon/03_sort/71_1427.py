n=list(map(int,str(input())))   # 입력값을 받을 때부터 모든 수를 슬라이싱하여 리스트로 담는다.
n.sort(reverse=True)    # 내림차순 정렬

for i in n:
    print(i,end='')
