

def Revword3(text):

    sp = list(text)

    for i in range(len(sp)):

        if sp[i] == " ":

            left = 0
            right = len()

            while(left<right):

                temp = sp[left]
                sp[left] = sp[right]
                sp[right] = temp

                left+=1
                right-=1


    return " ".join(sp)



text = "Let's take LeetCode Contest"
print(Revword3(text))