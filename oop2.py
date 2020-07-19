#attrubutes are the characteristics of an object methods or operations we can perform on the object.
class Dog():
    #CLASS OBJECT ATTRIBUTE
    species = "mammal"

    #whenever you have a class where you're going to be doing is defining methods inside that class and the methods looks like functions inside of a class.
    #we does have __init__() method and it's called automatically right after the object has been created. So once we initialize the object, we actually call this method automatically.
    #each attribute in the class definition begins with a reference to the instance object amd that by convention is "self" keyword, which is baically saying refer to this particular instance of this object.
    def __init__(self, breed, name): #this is the most basic special method you can have for initialization
        #"self" here tells that this method refers to itself (itself being the actual calss object)
        #also we can pass another attributes to init method, we passed "breed"
        #breed here is the argument and the value is passed during the instantiation or initialization of  the class itself.
        self.breed = breed # when here we will run the code, it will through an error saying "__init__() missing 1 required positional argument: 'breed'", which now means, whenever I create an instance of the Dog class I require "breed" as an argument.
        self.name = name #this name on the right side of the equal sign refers to input name of the __init__(name) method, self.name is kind of assigning the dog name to the initialization of that dog.

mydog = Dog(breed = "Lab", name = "Sammy") #let's provide the breed
#otherdog = Dog(breed = "Huskie")
print(mydog.breed) #note that they don't have close parantheses around breed. (like breed()). That's because it's an attribute, it's not a method I don't want to call it to action. I just want to report back what that attribute is.
#print(otherdog.breed)
print(mydog.name)
print(mydog.species)
#if you're really comfortable with an object nad you tend t ouse it a lot we'll end up seeing something more along the lines of this where you just say lab and sammy,
# they have to go in the correct order to be assigned to breed and name.
#mydog = Dog("Lab", "Sammy")
#CLass attributes are always the same for any instance of the class.
"""
Methods are functions defined inside the body of a class.
They're used to perform operations with the attributes of our objects and Methods are essential in encapsulation concepts of the OOP
This is essential in dividing the responsibilities in programming especially in lanrge applications
In this case methods are kind of the whole point of view would  want to create your object.
Methods basically are going to allow us to perform actions based off the attributes of the object.
"""

class Circle():
#we will say regardless of what  kind of circle you have, th pi that special number is always going to be p =3.14 for our estimated
    pi = 3.14
    def __init__(self, radius=1):
        self.radius = radius
#lets create the method that calculate the area of a Circle
    def area(self):
        #it's not just some free floating function inside of this class, it's actually a method of that class and that's what the self keyword is doing.
        return self.radius * self.radius * Circle.pi #here a lot of beginners make mistake
#the probleem here is what radius are you talking about? Are you talking about  the circles radius or some variable called radius
#the way to make sure that you know you're talking about the circles own radius when you actually instantiate it, it is need to say: self.radius and that tells this method.
    # let's make a very simple method that says set radius
    def set_radius(self, new_r):
        self.radius = new_r # I'm not returning anything and that's OK
        #Now all object methods need to return something. Some object methods just affect the object in place.


myc = Circle(3)
print(myc.radius)
print(myc.area) # the result of the running this would be: <bound method Circle.area of <__main__.Circle object at 0x03530C10>>
#it's particular instance of the circle class object located at this position: 0x03530C10 in my computer's memory
#if I actually want to execute this method I need to just like I would for a function have a set of open and closed parentheses around it
print(myc.area())
myc.radius = 100 # I redefine the radius
print(myc.area())
myc. set_radius(999)
print(myc.area())
#Now let's imagine that I want to have a method that allows me to reset the radius
#So there's two ways you can change attributes of a class in Python.
#One way is just call it directly off the object itself.
#The othed way you can create methods that reset object attributes.
#which way to choose it's up to you. It's a Programming style coice that is all right
