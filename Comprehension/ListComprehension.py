
a = [1,2,3,4,5,6,7,8,9]

result = [i for i in a if i%2==0]
print(result)

squ = [i**2 for i in a]
print(squ)

w = [ i**2 for i in range(1,6)]
print(w)

p = [ "Even" if num %2==0 else "Odd" for num in range(1,10)]
print(p)


s = "Python is a Language"
vowels = "aeiouAEIOU"

d = [i for i in s if i in vowels]
print(d)

