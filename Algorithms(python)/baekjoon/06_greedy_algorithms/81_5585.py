price=int(input())  
change=1000-price   #거스름돈
coins=[500,100,50,10,5,1]   

sum=0   

for i in coins: 
    change%=i

print(sum)