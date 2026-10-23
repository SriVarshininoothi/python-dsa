class Car:

    def __init__(self,color,brand,speed):

        self.color = color
        self.brand = brand
        self.speed = speed

    def start(self):
        print(self.brand,"is starting")


    def show_details(self):
        print("Color: ",self.color)
        print("Brand: ",self.brand)
        print("Speed: ",self.speed)

#create Objects

car1= Car("Red","Audi",140)
car2 = Car("Blue","BMW",100)

#Call Methods
car1.start()
car1.show_details()
print()

car2.start()
car2.show_details()
print()