num=[0,1,2,3,4,5]

print(' '.join(map(str,num)))
print(''.join(map(str,num)))
print('-'.join(map(str,num)))
# join은 문자열 리스트를 [n,n,n, ...] 형식이 아닌 []없이 원소들 사이에 '사이의 문자열을 추가하여 출력하는듯함 
print(str(num),sep='-')