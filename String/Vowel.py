name = input("enter a text: ")
name = name.lower()
vcount = 0
ccount = 0
count=0

# for ch in name:
#     if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
#         count=count+1
# print(count)


for w in name:
    if(w in 'aeiou'):
        vcount+=1
    else:
        ccount+=1

print(f"Vowels: {vcount}")
print(f"Consonants: {ccount}")
    


for i in name:
    if i in '0123456789':
        count = count+1
print(f"Digits: {count}")

scount = 0

for i in name:
    if i in " ":
        scount+=1
print(f"Space count : {scount}")
