
def RevString_PositionK(s,k):

    sp = list(s)
    for i in range(len(sp)):
        if(i==k):
            left=0
            right = i-1

            while(left<right):
                temp=sp[left]
                sp[left]=sp[right]
                sp[right]=temp

                left+=1
                right-=1

    return "".join(sp)
s = "abcdefg"
k = 2
print(RevString_PositionK(s,k))


     