x = 35

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


x = 50
def func(x):
    print('x is:', x)
    x = 1000 #local to our function now
    print('local x is changes to: ', x )

func(x)
print(x) 
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
