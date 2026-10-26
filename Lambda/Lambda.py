

#Addition

x = lambda a: a+10
y = lambda b : b-10
z = lambda c:c*2
w = lambda d:d/2

print(x(10))
print(y(10))
print(z(4))
print(w(7))



#square

s = lambda x:x**2
print(s(4))

#map

w = [1,2,3,4,5,6]
res = list(map(lambda x:x**2,w))
print(res)

#filter

even = list(filter(lambda y:y%2==0,w))
print(even)

#celsius

c =[0,10,20,30,40]

f = list(map(lambda x: x*(9/5)+32,c))
print(f)


s = ["racecar","hello","madam","python","noon"]
palind = list(filter(lambda p:p==p[::-1],s))
print(palind)



