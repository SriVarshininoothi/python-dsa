
res = {i:i**2 for i in range(1,6) if i%2==0}
print(res)


res = {i:i**3 for i in range(1,6)}
print(res)


a = ["Texas","California","Florida"]
b = ["Austin","Sacremento","Tallahassee"]

res = { state:captial for state,captial in zip(a,b)}
print(res)

product = ["Laptop","Mouse","Keyboard","Mointor","UseCable"]
price=[72000,250,1000,40000,1200]

result = { product: price for product,price in zip(product,price)}

condi = { i:j for i,j in result.items() if j>1000}
print(result)
print(condi)


a = {'a':1,'b':2,'c':3}

invert = {v:k for k,v in a.items()}
print(invert)


input = "banana"

freq = { char: input.count(char) for char in input}
print(freq)

q = {i: ("Even" if i%2==0 else "Odd") for i in range(1,6)}
print(q)