
# class Employee:

#     def work(self):
#         print("Employee is working ")

# class Developer(Employee):
#     def execute(self):
#         super().work()

#     def work(self):
#         print("Developer is working ")


# class Tester(Employee):

#     def work(self):
#         print("Tester is working ")

# e = Developer()
# e.work()
# e.execute()

class PaymentProceesor:

    def process_payment(self,amount):
        print("Payment amount")

class CreditCardPayment(PaymentProceesor):

    def process_payment(self,amount):
        print(f"Credit card {amount}")

class PayPalPayment(PaymentProceesor):

    def process_payment(self,amount):
        print(f"paypal {amount}" )

class CrypoPayment(PaymentProceesor):

    def process_payment(self,amount):
        print(f"Crypo {amount}" )    

def make_payment(self,amount): #Helper or utility function
    self.process_payment(amount)
    
c = CreditCardPayment()
p =PayPalPayment()
cp = CrypoPayment()

make_payment(c,160)
make_payment(p,500)
make_payment(cp,400)
