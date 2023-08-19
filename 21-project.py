
number = int(input("number: "))

if (number >0) and (number<=100):
    print("number in range")

else:
    print("number is not in range")    

#########

number = int(input("number: "))

if (number>0) and (number % 2 == 0):
    print("is positive and an even number")

else:
    print("positive and not even numbers")

#########    

number = int(input("number: "))

if (number>0):
    if (number % 2 == 0):
        print("is positive and an even number")
    else:
        print("number is positive but odd")    

else:
    print("number is negative")

#########

email = 'email@sadikturan.com'
password = 'abc123'

enteredEmail = input('email : ')
enteredPassword = input('password : ')

if (email == enteredEmail):
    if (password == enteredPassword):
        print("Email and password are correct")
    else:
        print("wrong password")    
else:
    print("wrong email")

########

a = int(input("a  : "))
b = int(input("b  : "))
c = int(input("c  : "))

if (a > b) and (a > c):
    print(f'a larger   ')

elif (b > a) and (b > c):
    print(f'b larger   ')

elif (c > a) and (c > b):
    print(f'c larger   ')

#########

exam_grade_1 = int(input("exam grade 1 : "))
exam_grade_2 = int(input("exam grade 2 : "))
final_grade = int(input("final grade : "))

average = (((exam_grade_1 + exam_grade_2) / 2) *0.6)  + (final_grade * 0.4) 

if (average>=50) and (final_grade>=50):
    print("you passed")

else:
    print("you not passed")

#########

name = (input("name  : "))
kilo = float(input("kilo  : "))
size = float(input("size  : "))

index = (kilo) /( size **2)

if (index >=0) and (index <=18.4):
    print(f'{name} kilo index: {index} and weight assessment weak :')

elif (index > 18.4) and (index <=24.9):
    print(f'{name} kilo index: {index} and weight assessment normal : ')

elif (index >=24.9) and (index <=29.9):
    print(f'{name} kilo index: {index} and weight assessment fat : ')

elif (index >=29.9) and (index <=34.9):
    print(f'{name} kilo index: {index} and weight assessment obese : ')

else:
    print("your information is wrong")

