
#######

number1 = int(input("number 1 : "))
number2 = int(input("number 2 : "))

result = (number1 > number2)
print(result)

#######

exam_grade_1 = int(input("exam grade 1 : "))
exam_grade_2 = int(input("exam grade 2 : "))
final_grade = int(input("final grade : "))

grade = (exam_grade_1 + exam_grade_2) / 2 
grade2 = grade % 60
grade3 = final_grade % 40
grade4 = grade2 + grade3

result = grade4 >= 50 
print("you passed" , result)

#######

number = int(input("number  : "))

result = number % 2 == 0
print("Is the number odd?", result)

#######

number = int(input("number  : "))
result = (number > 0)
print(result)

#######

email = 'email@sadikturan.com'
password = 'abc123'

enteredEmail = input('email : ')
enteredPassword = input('password : ')

isEmail = (email == enteredEmail.lower())
isPassword = (password == enteredPassword)

print(isEmail,isPassword )