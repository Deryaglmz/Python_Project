
x = 6

result = 5 < x < 10

# and
# True, True => True
# True, False => False
result = (x > 5) and (x < 10)

# or
# True, False => True
# True, True => True
# False, False => False
result = (x > 0) and (x % 2 == 0)

# not
result = not(x > 0)

result = ((x>5) and (x<10) and (x%2 == 0))

print(result)

############

number = float(input("number  : "))
#result = 0 < number < 100
result = (number > 0) and (number <=100)
print(result)

###########

number = int(input("number  : "))
result = (number > 0) and (number %2 == 0)
print(result)

###########

email = 'email@sadikturan.com'
password = 'abc123'

enteredEmail = input('email : ')
enteredPassword = input('password : ')

result = (email == enteredEmail) and (password == enteredPassword)

print(result)

###########

a = int(input("a  : "))
b = int(input("b  : "))
c = int(input("c  : "))

result = (a > b) and (a > c)
print(f'a larger :  , result')

result = (b > a) and (b > c)
print(f'b larger :  , result')

result = (c > a) and (c > b)
print(f'c larger :  , result')

###########

exam_grade_1 = int(input("exam grade 1 : "))
exam_grade_2 = int(input("exam grade 2 : "))
final_grade = int(input("final grade : "))

average = (((exam_grade_1 + exam_grade_2) / 2) *0.6)  + (final_grade * 0.4) 

#result = (average>=50) and (final_grade>=50)
result = (average>=50) or (final_grade>=50)
print("you passed" , result)

##########

name = (input("name  : "))
kilo = float(input("kilo  : "))
size = float(input("size  : "))

index = (kilo) /( size **2)
weak = (index >=0) and (index <=18.4)
normal = (index > 18.4) and (index <=24.9)
fat = (index >=24.9) and (index <=29.9)
obese = (index >=29.9) and (index <=34.9)

print(f'{name} kilo index: {index} and weight assessment weak : {weak}')
print(f'{name} kilo index: {index} and weight assessment normal : {normal}')
print(f'{name} kilo index: {index} and weight assessment fat : {fat}')
print(f'{name} kilo index: {index} and weight assessment obese : {obese}')

##########

# Indentity Operator : is

x = y = [1, 2, 3]
z = [1, 2, 3]

print(x==y)
print(x==z)
print(x is y)
print(x is z)

x = [1, 2, 3]
y = [2, 4]

del x[2]
y[1] = 1
y.reverse()

print(x==y)
print(x is y)
print(x is not y)

# Membership Operator: in

x = ['apple' , 'banana']
print('banana' in x)

name = 'Çinar'
print('a' in name)
print('a' not in name)

