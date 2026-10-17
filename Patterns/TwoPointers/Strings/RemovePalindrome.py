
def removePalindrome(text):

    if not text:
        return 0

    left = 0
    right = len(text)-1

    while(left<right):

        if(text[left]!=text[right]):

            return 2

        else:

            left+=1
            right-=1

    return 1





text = "ababa"
print(removePalindrome(text))