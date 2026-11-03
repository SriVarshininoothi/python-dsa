def RevStringTwo(s,k):

    sp = list(s)

    for i in range(0,len(sp),2*k):

        left = i
        right = min(i+k-1,len(sp)-1) 

        while(left<right):
            temp = sp[left]
            sp[left]= sp[right]
            sp[right]=temp

            left+=1
            right-=1

        return "".join(sp)


s = "abcdefg"
k = 2
print(RevStringTwo(s,k))

