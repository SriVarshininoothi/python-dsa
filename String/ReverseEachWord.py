
text = "Java is Easy"

split_text = text.split(" ")

new = ""

for i in split_text:

    reverse = i[::-1]
    new += reverse+" "

print(new)
    


