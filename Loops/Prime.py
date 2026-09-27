

n = int(input("enter your number: "))



count = 0
l = []

for i in range(1,n+1):

    if(n%i==0):
        count+=1
        l.append(i)

if(count<=2):
    print("Prime")
else:
    print("Not a Prime")


print(l)



