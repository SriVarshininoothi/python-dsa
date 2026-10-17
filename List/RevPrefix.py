def RevPrefix(text,ch):

    sp = list(text)

    for i in range(len(sp)):
        if sp[i] == ch:
            
            left = 0
            right = i


            while(left<right):

                temp = sp[left]
                sp[left] = sp[right]
                sp[right]= temp

                left+=1
                right-=1
            break

    return "".join(sp)
    


text = "abcdefd"
ch = "d"
print(RevPrefix(text,ch))