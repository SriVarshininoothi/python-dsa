
text = input()
t = list(text)

w = list(text) #copy of original text
left = 0
right = len(t)-1

while(left<right):

    temp = t[left]
    t[left] = t[right]
    t[right] = temp

    left+=1
    right-=1

if w == t:
    print("True")
else:
    print("False") 

    
    

