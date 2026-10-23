#Encapsulation Means protecting data inside a class
#It allows access to data only through class methods not directly

# class Bank:

#     def __init__(self):
#         self.__balance = 1000

#     def show_balance(self):
#         print(self.__balance)


#     def depost(self,amount):
#         self.__balance+=amount

#     def withdraw(self,amount):
#         self.__balance-=amount


# b = Bank()
# b.depost(3000)
# b.withdraw(1000)
# b.show_balance()


class Employee:

    def __init__(self,id,name,salary):

        self.__id = id
        self.__name=name
        self.__salary = 0

        self.update_salary(salary)

    def update_salary(self,new_salary):
        if new_salary > 0:
            self.__salary=new_salary
            print(self.__salary)
        else:
            print(f"Should not be negative salary")

    
    def display_employee(self):
        print(self.__id)
        print(self.__name)
        print(self.__salary)

e = Employee(1,"Rahul",34000)
e.update_salary(40000)
e.update_salary(-49)

e.display_employee()
