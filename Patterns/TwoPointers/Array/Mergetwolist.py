
# x = [1,3,5]
# y = [ 2,4,6]

# c = x+y
# d = sorted(c)
# print(d)


x = [1,2,3,5,7]
y = [2,3,4,7,8]

c = set(x)
d = set(y)

common = list(c&d)

print(common)