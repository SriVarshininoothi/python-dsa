
n = input("Enter a number: ")
m = input("Enter b number: ")

is_anagram = True

if len(n)!=len(m):

    is_anagram = False

else:

    for ch in n:

        if n.count(ch) != m.count(ch):
            is_anagram = False
            break

if is_anagram:
    print("Anagram")
else:
    print("Not anagram")




x = "abc"
y = "bca"


is_same = True

if len(x)!=len(y):
    is_same=False

else:
    for i in x:
        if x.count(i)!= y.count(i):
            is_same = False
            break
if is_same:
    print("yes")
else:
    print("No")



