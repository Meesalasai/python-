#the idea behind the object oriented programming
#So far we have the capability to create a very simple function or even a very complex function.
mylist = [1,2,3]
mylist.append(4)
print(mylist)
#what we don't know how to do is build something like a list object
#we don't know yet, how  can you build an object and then have methods inside of it or attributes inside of it that you can use ot affect the object itself.
#that's the whole idea of object oriented programming OOP - How we are able to actually create our own obects in Python
#we know how to use the built-in objects in Python but we don't know how to actually build our own.
#The first step on your journey of learning about OOP is to realize that in Python everything is an object and you can check an object type by saying type and then passing in an object itself
print(type([1,2,3]))
#it says me that it's the class "list" and class is going to be one of the keywords we use
#the class is essentially a blueprint that defines the nature of a future object and from classes we can then construct instances of that class
#an instance is just a specific object created for a particular class.
#let's see how we can actually use class
class Sample(): #functions are lowercase, functions starts with an uppercase
    pass #use pass to dot do anything
x = Sample()
print(type(x))
#Remember that everything in Python is object and we can built our own objects using the class keyword and we can ckech with the type built-in function what the actual class is
