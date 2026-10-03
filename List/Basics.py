
n = [30,50,70]

print(n)

#count
count = 0
for i in n:
    count +=1
print(count)


sum = 0
for i in n:
    sum+=i
print(sum)


marks = [1,2,3,4,5]
count = 0
for i in marks:
    if i%2==0:
        count+=1
print(count)


n = [3,2,2,1,2,4,1]

remove_dup = []

for w in n:

    if w not in remove_dup:

        remove_dup.append(w)
print(remove_dup)


dupl= []


for k in n:
    if n.count(k) > 1 and k not in dupl:
        dupl.append(k)
   
print(dupl) 




Input = [4, 2, 7, 2, 8, 4]
Input.sort()
rep=[]

for i in Input:
    if Input.count(i)>1 and i not in rep:
        rep.append(i)
        break

for j in rep:
    print(j)



 




     

     



      



