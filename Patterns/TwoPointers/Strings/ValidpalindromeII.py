def validPalindrome2(text):

    left =0
    right = len(text)-1

    while(left<right):
        if(text[left]!=text[right]):

            return checkPal(text,left+1,right) or checkPal(text,left,right-1)

        left+=1
        right-=1
    return True

def checkPal(text,left,right):

    while(left<right):
        if(text[left]!=text[right]):
            return False
        left+=1
        right-=1

    return True



text = input()
print(validPalindrome2(text))
