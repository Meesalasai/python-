# Finding Maximum of three numbers 
# int() is used for type conversion
# input() is used to take values from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
# compare number1 with number2 and number3 and prints the maximum number
if (num1 > num2) and (num1 > num3):
    print("Maximum number is: ", num1)
# compare number2 with number1 and number3 and prints the maximum number
elif (num2 > num1) and (num2 > num3):
    print("Maximum number is: ", num2)
# Above two condition fails then this condition executes and prints the maximum number.    
else:
    print("Maximum number is: ", num3)
