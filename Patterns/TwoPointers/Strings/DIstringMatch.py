
def DIMatch(text):

    sp = list(text)

    low = 0
    high = len(sp)
    
    res = []

    for i in sp:

        if i == "I":

            res.append(low)
            low+=1

        else:
            res.append(high)
            high-=1

    res.append(low)

    return res

text = "IDID"
print(DIMatch(text))