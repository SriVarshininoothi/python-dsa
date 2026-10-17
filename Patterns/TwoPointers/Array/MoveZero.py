
n = [0,1,0,3,12]

# l = []
# zer = []
# for i in n:

#     if i != 0:
#         l.append(i)
#     else:
#         zer.append(i)

# print(l+zer)


left = 0
right = 0

while(right<=len(n)-1):
    if(n[right]!=0):

        temp = n[left]
        n[left] = n[right]
        n[right]=temp
        

        left+=1
    right+=1

print(n)