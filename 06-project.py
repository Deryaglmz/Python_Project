#########

message = 'Hello there .  My name is Derya Gülmez'

message = message.upper()
message = message.lower()
message = message.title()
message = message.capitalize()

message = message.strip()
message = message.split('.')
message = ''.join(message)
message = '*'.join(message)

print(message[1])

index = message.find('Derya')

isFound = message.startswith('H')
isFound = message.endswith('z')
print(isFound)

message = message.replace('Derya', 'Pelin')
message = message.replace('ç', 'c').replace('ö', 'o').replace(' ', '-')

message = message.center(50)
message = message.center(100, '*')
print(index)

print(message)


##########

website ="http://www.sadikturan.com"
course = "Python Course : Python programming guide from start to finish (40 hours)"

result = 'Hello World'.strip()
result = 'Hello World'.rstrip()
result = 'Hello World'.lstrip()

result = website.lstrip('/:pth')

result= 'www.sadikturan.com'.strip('w.com')

result = course.lower()
result= course.upper()
result = course.title()

result = website.count('a')
result = website.count('www')
result = website.count('www', 0,10)

result = website.find('com')
result = website.find('com', 1,10)
result = course.find('Python')
result = course.rfind('Python')
result = website.index('com')
result = website.rindex('com')
#result = website.rindex('comm')    #exception 

result = course.isalpha()
result = 'Hello'.isalpha()
result = course.isdigit()
result = course.isdigit()
result = '123'.isdigit()

result = 'Contents'.center(50,'*')
result = 'Contents'.ljust(50,'*')
result = 'Contents'.rjust(50,'*')

result = course.replace(' ', '-')
result = course.replace(' ', '-',5)
result = course.replace(' ', '')

result = 'Hello World'.replace('World', 'There')
result = result[2]
result = result[5]

print(result)

