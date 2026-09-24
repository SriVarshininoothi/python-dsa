

#ATM

Options = int(input("Enter Option"))

user_pin = 1749


for i in range(1,4):
    pin = int(input("Enter your pin: "))

    if pin==user_pin:
        print("Accepted")
        break
    else:
        print("Incorrect PIN.")



