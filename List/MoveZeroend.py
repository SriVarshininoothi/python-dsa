
Input =  [0, 1, 0, 3, 12]

Zero = []
Rem = []


for i in Input:

    if  i == 0:

        Zero.append(i)

    else:
        Rem.append(i)

Rem.extend(Zero)
print(Rem)


Input = [2, -4, 5, -1, 3]


Neg = []
pos =[]

for i in Input:

    if i<0:

        Neg.append(i)
    else:
        pos.append(i)

Neg.extend(pos)
print(Neg)


n = [1,2,3,5]

r = []

for i in range(1,5):

    if i not in n:

        r.append(i)
print(r)


m = [1, 2, 3, 4]
n = [3, 4, 5, 6]

res = []

for i in m :

    if i in n:

        res.append(i)
print(res)



a = [2,7,11,15]

target = 9
sum = 0

result = []

for i in a:

    for j in a:
        
        sum=i+j

        if sum == target:
            result.append(i)
print(result)




b = [1, 2, 3, 4, 5]
k = 2

f_sp = b[:-k]
s_sp = b[-k:]

print(s_sp+f_sp)








