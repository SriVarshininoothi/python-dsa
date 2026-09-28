import math
n = int(input("enter a n: "))

m = str(n)
l = len(m)
sum = 0

for i in m:
    digit = int(i)
    sqr = int(math.pow(digit,l))
    sum = sum+sqr

if n==sum:
    print(f"{n} is an Armstrong number")
else:
    print(f"{n} is not an Armstrong ")