#INHERITANCE
#Inheritance is a way to form new classes using older classes that have already been defined.
# that way newly formed classes are called "derived" classes and the classes that we "derive" from are base classes
# So derive from the base class important benefits of inheritance our code reuse and reduction in the complexity of a program that we don't have to constantly be creating duplicate classes
# you can just inherit from another class and use some of the methods that are available there.
class Animal():

    def __init__(self):
        print("ANIMAL CREATED") #ususally you don't have the print statement in the initialization method

    def whoAmI(self):
        print("ANIMAL")

    def eat(self):
        print("EATING")

class Dog(Animal):

    def __init__(self):
        #Animal.__init__(self) #it means initialize an animal and then we say print them created
        print("DOG CREATED")

    def bark(self):
        print("WOOF")

    def eat(self):
        print("DOG EATING")

mya = Animal() #ANIMAL CREATED
mya.whoAmI() #ANIMAL
mya.eat()   #EATING

myd = Dog() #shows DOG CREATED
myd.whoAmI() #ANIMAL
myd.eat()   #EATING
myd.bark()
#So even though the class "Dog" dosn't have whoAmI() or eat() methods inside of it, it was able to inherit those methods or derive from the base class of animal.
#That's the entire idea behind inheritance is the fact that you can inherit  from another class or derive another class
#I can also overwrite classes so I'm not strictly limited to everything that was an ANIMAL


#SPECIAL METHODS
#Special methods are basically going to allow you to perform special operations and these methods are not actually called directly but they're called by specific Python language syntax.
#Imagine that I create a list
mylist = [1,2,3]
print(mylist)

#I'm going to create a class:
class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        #return "hello"
        #but if we want to return actually something that make sence:
        return "Title: {}, Author: {}, Pages: {}".format(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("a book is destroyed!")

b = Book("Python", "jose", 200)
print(b) # it prints: <__main__.Book object at 0x010A04C0>

#when we call the print() function on an object is it looks for it's string representation
 #and right now we haven't actually scpecifically defined the books string representation
 #we need to use what's known as a "special method" to do that and all special methods inside of a class
 #and all the special methods inside of a class are annotated with two underscores the name of the special method and then two extra __(underscores) __str__()
 #ANd this special method __str__() is the representation of my object.
 #So whenever a function asks for the the string representation of my object and the print function does that, it will return whatever here to return

#other special method len:(__len__)
len([1,2,3]) # it will get 3. But what happens if  I call:
len(b) #TypeError: object of type 'Book' has no len()
##after adding __len__(self) function:
print(len(b)) #will show 200 in the result because pages are 200
##and __del__(). the way you can delete the object from memory space is with this method and then whatever the object name
del b
