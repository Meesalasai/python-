# Program to find simple interest
# float() is used for type conversion 
# input() is used to take values from the user
P = float(input("Enter principal amount: "))
T = float(input("Enter time: "))
R = float(input("Enter Rate of interest: "))
#In general Simple Interest formula is ((principal * time * rate)/100)
SI = ((P * T * R) / 100)
# Prints the simple interest value
print("simple interest is", float(SI)) 
