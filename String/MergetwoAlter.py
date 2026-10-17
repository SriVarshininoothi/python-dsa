def MergeTwoAlter(s1,s2):

    p1 = 0 
    p2 = 0
    res = []

    while(p1<len(s1) and p2<len(s2)):
        res.append(s1[p1])
        res.append(s2[p2])
        p1+=1
        p2+=1

    while(p1<len(s1)):
        res.append(s1[p1])
        p1+=1

    while(p2<len(s2)):
        res.append(s2[p2])
        p2+=1

    d = "".join(res)

    return 

s1 = "xyzio"
s2 = "abc"
print(MergeTwoAlter(s1,s2))