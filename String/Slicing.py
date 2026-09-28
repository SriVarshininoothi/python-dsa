

text = "Python is a Programming Language"

print(text[2:])
print(text[:2])
print(text[:])
print(text[::2])
print(text[::-1])

#String immutability

name = "Python"

name = 'Q' + name
print(name)

#Concatenation

first = 'Hello'
second = 'Python'

result = first+" "+second
print(result)

#Repetition

print("Hi "*3)


#String Methods

name = "PytHon"

lower = name.lower()
print(lower)


upper = name.upper()
print(upper)

extra = " Welcome   "
print(extra.strip())


r = "I like Java"
print(r.replace("Java","Python"))
print(r.replace(" ","-"))

#split

words = r.split()
print(words)


#join

result = " ".join(words)
print(result)

#find

print(text.find("Python"))
print(r.find("Java"))


#count
input = "hello"
print(len(input))
print(result.count("a"))


#startswith and endswith()


filename ="data.csv"
print(filename.startswith("data"))
print(filename.endswith(".csv"))


#String Formatting

name = "Sri"
age = 22

print(f"My name is {name} and I am {age}")


a = 10
b= 20

print(f"total = {a+b}")


#format

print("My name is {} and I am {}.".format(name,age))