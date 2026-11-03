
def Revser_digit(s):

    e = list(s)
    left = 0
    right = len(e)-1

    while(left<right):

        while(left<right and not e[left].isalpha()):
            left+=1

        while(left<right and not e[right].isalpha()):
            right-=1

        if(e[left]!=e[right]):
            temp = e[left]
            e[left]=e[right]
            e[right]=temp

        left+=1
        right-=1

    return "".join(e)



s = "ab-cd"
print(Revser_digit(s))