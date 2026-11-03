#iterable


n = [10,20,30,40]
for num in n:
    print(num)

#iterator

n = [10,30,40]

it = iter(n)
print(next(it))
print(next(it))
print(next(it))
#print(next(it)) # stopiteration error


text ="ACT"

iterator = iter(text)
print(next(iterator))
print(next(iterator))
print(next(iterator))


# Custom iterator

class MyNumbers:

    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):

        if self.num <= 5:
            value = self.num
            self.num +=1 
            return value
        else:
            raise StopIteration

obj = MyNumbers()
itr = iter(obj)

for i in obj:

    print(i)



# Even Number

class Even_number:

    def __iter__(self):
        self.num = 2
        return self

    def __next__(self):

        if self.num <= 10:
            value = self.num
            self.num +=2
            return value
        else:
            raise StopIteration

obj = Even_number()
itr = iter(obj)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))