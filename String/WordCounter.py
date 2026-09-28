
text = "Python is easy to learn"

words = text.split(" ")
print(len(words))


#particular
print(text.find('e'))


#first Appear twice
repeat = ""
for ch in text:
    if text.count(ch) > 1:
        repeat+=ch
        break
print(repeat)


#non repeating 

Not_Repeat = ""
for ch in "swiss":
    if text.count(ch)<1:
        Not_Repeat+=ch
        break
print(Not_Repeat)

