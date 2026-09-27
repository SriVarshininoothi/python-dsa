
n = int(input("enter a number: "))

mul = 1
count=0
l = []

for i in range(1,n+1):
    if(n%i==0):
        mul=i
        count+=1
        l.append(mul)
        
print(l)      
print(count)

        