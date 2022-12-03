doc=input()
word=input()
count=0
n=0

while(n<=len(doc)): # len(doc)-len(word)라고 해도 맞음
    if(doc[n:n+len(word)]==word):  
        count+=1
        n+=len(word)
    else:
        n+=1

print(count)
