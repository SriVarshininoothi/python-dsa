units = int(input("Enter units: "))

charges = 0.0

if(units>=0 and units<=50):
    charges=1.95 * units
elif(units>=51 and units<=100):
    charges=(50 * 1.95) + ((units-50) * 3.10)
elif(units>=101 and units<=200):
    charges=(50 * 1.95) + (50 * 3.10) + ((units-100) * 4.80)
elif(units>=201 and units<=300):
    charges=(50 * 1.95) + (50 * 3.10) + (100 * 4.80) + ((units-200) * 7.70)
elif(units>=301):
    charges=(50 * 1.95) + (50 * 3.10) + (100 * 4.80) + (100 * 7.70) + ((units-300) * 9.00)

fixed_charges = 20
customer_charges = 100
electricity_duty = units * 0.06

total = charges + fixed_charges + customer_charges + electricity_duty

print("Energy Charges:", charges)
print("Fixed Charges:", fixed_charges)
print("Customer Charges:", customer_charges)
print("Electricity Duty:", electricity_duty)
print("Total Bill:", total)