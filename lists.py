mylist = [1,2,3]
mylist2 = ['stringdjkd', 1,2,3,4, True, 'asdf', [1,2,3], 23.54]
print(mylist)
print(mylist2)
print(len(mylist2))

print(mylist2[-1])
print(mylist2[2:])
print(mylist2[:3])

mylist3 = ['a', 'b', 'c', 'd', 'e', 'f']
mylist3.append("NEW ITEM")
mylist3.append(['x','y','z'])
print(mylist3)

mylist4 = ['a', 'b', 'c', 'd', 'e', 'f']
listtwo = ['x', 'y', 'z']
mylist4.extend(listtwo)
print(mylist4)

mylist5 = ['a', 'b', 'c', 'd', 'e', 'f']
item = mylist5.pop()
print(mylist5)
print(item)
mylist6 = ['a', 'b', 'c', 'd', 'e', 'f']
item2 = mylist6.pop(0)
print(mylist6)
print(item2)

mylist7 = ['a', 'b', 'c', 'd', 'e', 'f']
mylist7.reverse()
print(mylist7)

mylist8 = [3,6,8,5,4,0,2,7,1,9]
mylist8.sort()
print(mylist8)

mylist9 = [1,2,['x','y','z']]
print(mylist9[2])

matrix = [[1,2,3],[4,5,6],[7,8,9]]
first_col = [row[0] for row in matrix]
print(first_col)
