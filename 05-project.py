
######

website ="http://www.sadikturan.com"
course = "Python Course : Python programming guide from start to finish (40 hours)"

print(len(course))

print(website[7:10])

print(website[21:24])

print(course[-15:])

print(course[::])    #takes the whole text
print(course[::-1])

result = course[::-1]
s= '123450' * 5
print(s)
print(s[::5])


######

name = 'Bora'
surname = 'Yılmaz'
age = 32
job = "Engineer" 

print("My name is {} {} , Im {} years old , I am an {} . ".format(name,surname,age,job))
print(f"My name is {name} {surname} , Im {age} years old , I am an {job} .")


#######

s= ("Hello world")
s= s[0:6] + 'W' + s[-4:]

print(s)

######

s= 'abc ' * 3
print(s)