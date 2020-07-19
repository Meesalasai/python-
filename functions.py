def my_func(param1 = 'default'):
    """
    THIS IS THE DOCSTRING
     this function returns a string with deafult
    """
    print("my first python function! {}".format(param1))

my_func()

#difference between return and printing from the function
def hello():
    print("hello")
hello()

def hello1():
    return "hello"
hello1()
result = hello1()
print(result)

def addNum(num1,num2):
    return num1+num2
result = addNum(2,3)
print(result)
print(type(result))
#more realistic error code
result = addNum("2", "3")
print(result)
print(type(result))

#simple example of nice checking:
def addNum(num1,num2):
    if type(num1)==type(num2)==type(10):
        return num1+num2
    else:
        return "Sorry, I need integers"

result = addNum('2','3')
print(result)


#lambda expression

#Filter
mylist = [1,2,3,4,5,6,7,8]

def even_bool(num):
    return num%2 == 0 # it's going to return True if the number is even and False if it's odd.

evens = filter(even_bool, mylist)
print(list(evens))
print(evens)

#write all that with lambda expression:
lambda num:num%2 ==0
evens = filter(lambda num:num%2 ==0, mylist)
print(list(evens))
print(evens)

#string methods
st = 'hello'
st.lower()
st.upper()
st.split()

tweet = "Go Sports! #Sports"
result = tweet.split("#")
print(result)

#in key word
'x' in [1,2,3]
print('x' in [1,2,3])
print('x' in [1,2,3, 'x'])
