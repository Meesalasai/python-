# program to find compound interest
# int() and float() is used for type conversion 
# input() is used to take values from the user

principle = int(input("Enter principal amount : "))
time = int(input("Enter time : "))
rate = float(input("Enter rate : "))
# A function is created by name compound interest with the parameters principal,time and rate.
# Formula for compound interest is (principle * (1 + rate / 100)power(time)))
def compound_interest(principle, time, rate):  
	CI = principle * (pow((1 + rate / 100), time)) 
	print("Compound interest is", CI) 
 
compound_interest(principle, time, rate) 
