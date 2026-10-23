class Robot:

    def __init__(self,name,color,battery):
        self.name = name
        self.color = color
        self.battery = battery

    def say_hello(self):

        print("Hello",self.name)

    def show_Status(self):

        print(self.name)
        print(self.color)
        print(self.battery)

robot1 = Robot("Chitti","Red",80)
robot2 = Robot("Potti","Blue",78)

robot1.say_hello()
robot1.show_Status()
print()


robot2.say_hello()
robot2.show_Status()
print()

