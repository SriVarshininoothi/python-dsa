name = input("enter a text: ")
name = name.lower()
count = 0

# for ch in name:
#     if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
#         count=count+1
# print(count)


for w in name:
    if(w in 'aeiou'):
        count+=1
print(count)