
l = [51,10,35,46]

left = 0
right = len(l)-1

while(left<right):

    temp = l[left]
    l[left] = l[right]
    l[right]= temp


    left+=1
    right-=1

print(l)

