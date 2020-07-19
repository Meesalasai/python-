try:
    f=open('simple.txt', "r") #if we return "w" to "r" we will get the error
    f.write("Test write to simple test")
except IOError: #you don't need to specify specific error
    print("ERROR: COULD NOT FIND OR READ DATA")
finally:
    print("I ALWAYS WORK NO MATTER WHAT!")


# else:
#     print("SUCCESS!")
#     f.close()
