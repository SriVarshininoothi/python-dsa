def CheckWOrd(w,s):

    sp = w.split()

    for i in range(len(sp)):
        if sp[i].startswith(s):
            return i+1
    return -1
        

w = "i love eating burger"
s ="burg"

print(CheckWOrd(w,s))