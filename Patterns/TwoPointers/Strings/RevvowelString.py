
def ReverseVowel(s):

    sp = list(s)
    left = 0
    right = len(sp)-1
    vowels = "aeiouAEIOU"

    while(left<right):
        while(left<right and sp[left] not in vowels):
            left+=1
            
        while(left<right and  sp[right] not in vowels):
            right-=1

        if(sp[left]!=sp[right]):
            temp= sp[left]
            sp[left]=sp[right]
            sp[right]=temp

        left+=1
        right-=1

    return "".join(sp)
s = "Icecream"
print(ReverseVowel(s))

    


