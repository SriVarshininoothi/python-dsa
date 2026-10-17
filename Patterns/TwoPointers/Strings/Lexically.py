def lexicallySmall(n):

    l = list(n)

    left = 0
    right = len(l)-1

    while(left<right):

        if(l[left]!=l[right]):

            smallest =  l[left] if l[left] < l[right] else l[right]

            l[left]  = smallest 
            l[right] = smallest

        left+=1
        right-=1
    
    return "".join(l)

s = "etcfe"
print(lexicallySmall(s))
