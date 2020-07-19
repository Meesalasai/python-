unit1 = input("Which unit you would like to convert from please choose between hour,minutes,seconds and day : ")
unit2 = input("Which unit you would like to convert to please choose between hour,minutes,seconds and day : ")
i = float(input("Enter value: "))

if unit1 == "seconds" and unit2 == "minutes":
    print("%s minutes " %(i/60))
elif unit1 == "seconds" and unit2 == "hour":
    print("%s hour" %(i/3600))
elif unit1 == "minutes" and unit2 == "seconds":
    print("%s seconds" %(i * 3600))
elif unit1 == "minutes" and unit2 == "hour":
    print("%s hour" %(i/60))
elif unit1 == "hour" and unit2 == "minutes":
    print("%s minutes" %(i * 3600))
elif unit1 == "hour" and unit2 == "seconds":
    print("%s seconds" %(i * 3600))
elif unit1 == "day" and unit2 == "hour":
    print("%s hour" %(i * 24))
elif unit1 == "day" and unit2 == "minutes":
    print("%s minutes" %(i * 1440))
elif unit1 == "minutes" and unit2 == "day":
    print("%s day" %(i / 1440))
