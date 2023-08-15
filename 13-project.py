#set 

fruits = {'orange', 'banana', 'apple'}

#print(fruits)

for x in fruits:
    print(x)

fruits.add('cherry')    
fruits.update(['mango', 'grape'])

fruits.remove('mango')   #delete
fruits.discard('apple')  #delete
print(fruits)

fruits.pop()
print(fruits)
fruits.clear()

myList = [1,2,5,4,4,2,1]
print(myList)
print(set(myList))
