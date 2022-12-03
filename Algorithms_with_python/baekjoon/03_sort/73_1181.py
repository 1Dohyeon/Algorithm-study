# input()을 이용하여 푸는법

n=int(input())
arr=[]

for i in range(n):
    arr.append(str(input()))

set_arr=set(arr)    # set함수로 중복된 값을 제거한다.  
arr=list(set_arr)   # set은 집합이므로 순서가 없다. 다시 리스트형식으로 바꿔준다. 

arr.sort()  # 2번째 조건부터 맞추고 첫번째 조건을 맞춘다.
arr.sort(key=len)

for i in arr:
    print(i) 


'''

import sys

n=int(sys.stdin.readline())
arr=[]

for i in range(n):
    arr.append(str(sys.stdin.readline().strip()))   # strip함수로 문자열 앞뒤를 제거한다.

set_arr=set(arr)    
arr=list(set_arr)  

arr.sort()  
arr.sort(key=len)

for i in arr:
    print(i) 
'''