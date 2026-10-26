import datetime

x = datetime.datetime.now()
print(x)


#creating 

y = datetime.datetime(2026,10,26)
print(y)


#strftime

z = datetime.datetime(2026,10,26)
print(z.strftime("%a"))
print(z.strftime("%A"))

print(z.strftime("%b"))
print(z.strftime("%B"))

print(z.strftime("%w"))
print(z.strftime("%d"))

print(z.strftime("%h"))