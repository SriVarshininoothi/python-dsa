def palindromeString(n):

    left = 0
    right = len(n)-1

    while(left<right):

        if(n[left]!=n[right]):
            return False

        left+=1
        right-=1

    return True


n = "madam"
print(palindromeString(n))