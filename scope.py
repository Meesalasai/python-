x = 25

def my_func():
    x = 50
    return x

print(x)
print(my_func())

#LOCAL
lambda x: x**2 #this particular x is local (local level)

#Enclosing function locals - this occurs when we have a function inside of another function (nested functions)
name = 'This is a global name!' #global - because it's not inside of any function it's at the top level of the scope.py file(which is cometimes also known as a module)

def greet():
    name = "Sammy"

    def hello():
        print("Hello " + name)
    hello()
greet()
print(name)

#Built-in level
#Buil-it functions you should never over-write here
len
#When you declare variables inside of a function definition they are not related in any way to other variables with the same names used outside of the function
#All variables have the scope of the block they're declare in starting from the point definition of the name.
x = 50
def func(x):
    print('x is:', x)
    x = 1000 #local to our function now
    print('local x is changes to: ', x )

func(x)
print(x) #here Python uses the value of the parameter declared in the main block above the function definition

#Imagine the situation when you're inside of the function and want to change the global # XXX:
 #so far it seems like you're only limited to changing the local x.
 #what if you actually wanted this function to reach out to the global level and rename x = 1000
 #how can we do that? - with the "global" keyword call.
 #It's recommended try to avoid using the global keyword because doing this if you have really long line of code or a large file of code can really mess up your namespace, if you're not super careful about it

def func2():
    global x
    x = 1000
print("Before function call, x is: ", x)
func2()
print("After function call, x is: ", x)
#instead of global key word, you should do is use "return" keywords.
def func3():
    #global x
    x = 1000
    return x
#and with this return, you can use it in global namespace
print("Before function call, x is: ", x)
x = func3()
print("After function call, x is: ", x)
