#If statements
if 1<2:
    if 2<3:
        print("True!")

if 1<2:
    print('First Block')
    if 20<3:
        print("Second Block")

if 1 >2:
    print("hello")
elif 3 == 3:
    print("elif ran")
else:
    print("last")

#loops
#for loops
seq = [1,2,3,4,5,6]
for jelly in seq:
    # code here
    print(jelly)

d = {"Sam":1, "Frank":2, "Dan":3}
for item in d:
    print(item)

for k in d:
    print(k)
    print(d[k])

mypairs = [(1,2),(3,4),(5,6)]
for item in mypairs:
    print(item)

for tup1, tup2 in mypairs:
    print(tup1)
    print(tup2)

#while loops:
i =1
while i<5:
    print("i is: {}".format(i))
    i = i+1

#range
for item in range(10):
    print(item)

#practical example
x = [1,2,3,4]
out = []
for num in x:
    out.append(num**2)
print(out)

#writing code above in the List comprehension
out = [num** 2 for num in x]
print(out)
