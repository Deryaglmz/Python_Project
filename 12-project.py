
students = {
    '120' : {
        'name' : 'Derya' ,
        'surname' : 'Gülmez',
        'telephone' : '555 000 00 01'
    },

    '125': {
        'name' : 'Pelin',
        'surname' : 'Deniz',
        'telephone' : '555 000 00 02'
    },

    '128' : {
        'name' : 'Cansu',
        'surname' : 'Güneş',
        'telephone' : '555 000 00 02'
    },
}

students ={}

number = input("student no :")
name = input("student name :")
surname = input("student surname :")
phone = input("student telephone :")

students[number] ={
    'name' : name,
    'surname' : surname,
    'telephone' : phone
}

print(students) 

students.update({
    number:{
        'name' : name,
        'surname' : surname,
        'telephone' : phone

    }
})

#print(students)

number = input("student no :")
name = input("student name :")
surname = input("student surname :")
phone = input("student telephone :")

students.update({
    number:{
        'name' : name,
        'surname' : surname,
        'telephone' : phone

    }
})

number = input("student no :")
name = input("student name :")
surname = input("student surname :")
phone = input("student telephone :")

students.update({
    number:{
        'name' : name,
        'surname' : surname,
        'telephone' : phone

    }
})

print('*'*50)

stdtNo = input('students no: ')
student = students[stdtNo]
print(student)

print(f"student number {stdtNo} student name : {student['name']} surname: {student['surname']} and telephone :{student[phone]}" )

