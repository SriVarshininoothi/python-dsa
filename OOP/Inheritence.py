

# class Employee:

#     def work(self):
#         print("Employee is working")

# class Developer(Employee):

#     def code(self):
#         print("Developer is coding")

# class Tester(Employee):

#     def test(self):
#         print("Tester is testing the app")


# d = Developer()
# d.work()
# d.code()

# t = Tester()
# t.test()
# t.work()



class Vechile:

    def __init__(self,brand,speed):
        self.__brand = brand
        self.__speed=speed

    def show_details(self):

        print(self.__brand)
        print(self.__speed)

class Car(Vechile):

    def __init__(self,brand,speed,seats):
        super().__init__(brand,speed)
        self.seats = seats

    def show_car_details(self):

        super().show_details()
        print(f"Seat {self.seats}")
    
class Bike(Vechile):

    def __init__(self,brand,speed,gear_count):
        super().__init__(brand,speed)
        self.gear_count = gear_count

    def show_bike_details(self):
        super().show_details()
        print(f"Gear: {self.gear_count}")

c = Car("BMW",100,4)
c.show_car_details()
    
b = Bike("Yahma",90,6)
b.show_bike_details()

        