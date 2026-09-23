
age = int(input("Enter age"))

if(age>60):
    print("Senior citizen")
elif(age>=23 and age<50):
    print("Adult")
elif(age>18 and age<23):
    print("Teenager")
else:
    print("Child")


marks = int(input("Enter your marks: "))

if(marks>=80 and marks<=90):
    print("A grade")

elif(marks>=70 and marks<=80):
    print("B Grade")

else:
    print("C Grade")