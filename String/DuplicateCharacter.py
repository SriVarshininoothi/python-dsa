

text = input("enter a text: ").lower()

visted = ""

w = ""
for i in text:

    if i not in visted:

        visted+=i
    else:
        w+=i

print(visted)
print(w)




