
Input = "Java is Powerfully"
sp = Input.split(' ')

max_len = 0
max_word = ""

for i in sp:
    l = len(i)

    if l > max_len:
        max_len = l

        max_word = i
print(max_word)



