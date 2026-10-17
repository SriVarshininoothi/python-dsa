

def ReverseString(s):

    sp = list(s)

    left = 0
    right = len(sp)-1

    while(left<right):
 
        sp[left],sp[right] = sp[right],sp[left]

        left+=1
        right-=1

    return "".join(sp)
s = "hello"
print(ReverseString(s))