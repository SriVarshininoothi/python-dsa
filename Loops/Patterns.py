

n = int(input("enter a number: "))


for i in range(1,n+1):

    for j in range(i):

        print("* ",end=" ")
    print() 

 

for i in range(1,n+1):

    for j in range(n-i):

        print("* ",end=" ")
    print() 



for i in range(1,n+1):

    for j in range(1,i+1):

        print(j,end=" ")
    print() 


for i in range(1,n+1):

    for j in range((n-i)):

        print(j,end=" ")
    print() 


for i in range(1,n+1):

    for j in range(i):

        print(i,end=" ")
    print() 


for i in range(1,n+1):

    for j in range((n-i)):

        print(" ",end=" ")

   
    for k in range(i):
        print("*",end=" ")
    
    print() 