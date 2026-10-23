from abc import ABC , abstractmethod

#abc = abstract base class
class ATM(ABC):
    @abstractmethod  #abstractmethod make this function abstract no return type

    def withdraw(self):
        pass

class SBI(ATM):

    def withdraw(self):
        print("Money withdraw from SBI")

class Axis(ATM):
     def withdraw(self):
        print("Money withdraw from Axis")


s = SBI()
a = Axis()

s.withdraw()
a.withdraw()
    