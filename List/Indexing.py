
marks = [80,75,92,68,88]

print(marks[0])

print(marks[1:4])
print(marks[:3])
print(marks[2:])

print(marks[::-1])

# updating

marks = [80,75,92]
marks[1] = 34
print(marks)

#append
marks.append(89)
print(marks)

#insert

marks.insert(4,78)
print(marks)

#remove
marks.remove(80)
print(marks)

#pop

marks.pop()
print(marks)

#clear
# marks.clear()
# print(marks)

marks.sort(reverse=True)
print(marks)

marks.sort()
print(marks)

marks.reverse()
print(marks)


matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matrix[0]
print(matrix)

matrix[0][1]
print(matrix)

matrix[2][2]
print(matrix)


matrix=[[10,20],[30,40]]

for row in matrix:
    for col in row:

        print(col)



