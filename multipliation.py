#Program to do Multiplication Table of a given  Number

num = int(input("Enter the number: "))
print("Multiplication Table of ", num)
for i in range(1, 21):
   print(num,"X",i,"=",num * i)
