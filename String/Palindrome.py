
text = input("Enter a text: ")

reverse = text[::-1]

if text == reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")