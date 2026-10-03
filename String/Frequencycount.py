
text = input("Enter a text : ").lower()

visited = ""
max_count = 0
max_char = ""

for ch in text:

    if ch not in visited:
        visited+=ch
        count = 0

        for i in text:

            if ch == i:
                count+=1

            if count>max_count:
                max_count=count
                max_char=ch


        print(f" {ch} = {count}")
print(f"Frequent max character: {max_char}")
        
 


