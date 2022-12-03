a,b,v=map(int,input().split())
day=(v-b)/(a-b)  # 올라가는데 걸리는 날짜의 최솟값을 구함
print(int(day) if day==int(day) else int(day)+1)    # 소수일 경우 하루가 지났다는 의미이므로 +1

