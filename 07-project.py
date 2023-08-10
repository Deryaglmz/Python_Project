######

message = 'Hello There . My name is Derya Gülmez'.split()
print(message)
print(message[0])

######

my_list = [1,2,3]
my_list= ['bir' , 2, True]
print(my_list)

######

list1= ['one', 'two', 'there']
list2 = ['four', 'five', 'six']

number = list1+ list2
print(number)
print(len(number))

######

usersA = ['Derya', 20]
usersB = ['Pelin', 19]

users = [usersA, usersB]

print(usersA)
print(usersB)
print(users)

print(users[0][0])

######

list1 = ['Bmw', ' Mercedes', 'Opel', 'Mazda'] 
 
result = (len(list1)) 

result = list1[0]
result = list1[3]
result = list1[-1]

list1[-1] = 'Toyota'
result = list1

result  = 'Mercedes' in list1

result = list1[-2]

result = list1[0:3]
result = list1[:3]
result = list1[-2:]

result[-2] = ['Toyota', 'Renault']
result = list1

result = list1 + ['Audi', 'Nissan']

del list1[-1] 
result = list1

result = list1[::-1]

######

studentA = ['Yiğit', 'Bilgi', 2010,[70,60,70]]
studentB = ['Ahmet', 'Sevim',1999,[80,80,70]]
studentC = ['Ahmet', 'Turan',1998,[80,70,90]]

result = studentA[0]
result = studentB[1]
result = studentC[3][1]

result = f"{studentA[0]} {studentA[1]} {2019-studentA[2]} age and grade point average {(studentA[3][0]) +(studentA[3][1]) + (studentA[3][2])} "

print(result)

######