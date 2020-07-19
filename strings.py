#indexing
mystring = 'Hello World'
print(mystring)
print(mystring[0])
#slicing
print(mystring[2:5])
print(mystring[::1])#print everything
print(mystring[::2]) #step two
#mystring[0] = "X" - not executable line because string is immutable

#basic methods
x = mystring.upper()
x = mystring.lower()
y = mystring.capitalize()
z = mystring.split()
e = mystring.split('e')
print(x)
print(y)
print(z)
print(e)

#print formatting
x = "Insert another string here: {}".format("INSERT ME!")
print(x)
y = "Item One: {}; Item Two: {};".format("dog", "cat")
print(y)
