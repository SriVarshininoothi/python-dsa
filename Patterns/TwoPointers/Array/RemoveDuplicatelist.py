
n = [1,1,2,2,3,4,4]


#loop
# vistied = []


# for i in n:
#     if i not in vistied:
#         vistied.append(i)
# print(vistied)

#set
# v = set(n)
# l = list(v)
# print(l)


#two pointers

left = 0
right = 1

while (right<= len(n)-1):

    if (n[right]!= n[left]):

        left+=1
        n[left]=n[right]
    right+=1

print(n[:left+1])    

