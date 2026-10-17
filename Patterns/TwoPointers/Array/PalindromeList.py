
text = [1,2,3,2,1,0]

g = list(text)

left = 0

right = len(text) - 1

while(left < right ):

    temp = text[left]
    text[left] = text[right]
    text[right] = temp

    left+=1
    right-=1

if g == text:
    print("True")
else:
    print("False")

