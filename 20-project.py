
name = input('Name: ')
age = int(input('Age: '))
education_information = input('Education information: ')

if (age >= 18) and (education_information == 'high school' or education_information =='university'):
    print("You can get a license")

else:
    print("You can't get a license")   
  
########

name = input('Name: ')
age = int(input('Age: '))
education_information = input('Education information: ')

if (age >= 18):
    if (education_information == 'high school' or education_information =='university'):
        print("You can get a license")
    
    else:
        print("You can't get a driver's license, your education level is insufficient")

else:
    print("You can't get a driver's license you are not old enough")  

########

written_note1 = int(input("written_note1: "))
written_note2 = int(input("written_note2: "))
verbal_grade = int(input("verbal grade: "))

average = (written_note1 + written_note2 + verbal_grade) / 3

if (average>=0) and (average<25):
    print(f'avarage: {average} your note: 0')

elif (average>= 25) and (average<45):
    print(f'avarage: {average} your note: 1')

elif (average>= 45) and (average<55):
    print(f'avarage: {average} your note: 2')    

elif (average>= 55) and (average<70):
    print(f'avarage: {average} your note: 3')

elif (average>= 70) and (average<85):
    print(f'avarage: {average} your note: 4')    

elif (average>= 85) and (average<100):
    print(f'avarage: {average} your note: 5')

else :
    print("you entered wrong information")        

##########

days = int(input("How many days has your vehicle been in traffic?"))

if days <=365:
    print("1 st service interval")

elif days>365 and days<=365*2:
    print("2 st service interval")

elif days>365*2 and days<=365*3:
    print("3 st service interval")    

else:
    print("wrong time")
  

import datetime

date = (input("What date was your vehicle on the road? (2019/8/9)"))
date = date.split('/')
traffic_exit = datetime.datetime(int(date[0])), (int(date[1])), (int(date[2]))
now = datetime.datetime.now()
difference = now - traffic_exit
days = difference.days
print(now - date )

if days <=365:
    print("1 st service interval")

elif days>365 and days<=365*2:
    print("2 st service interval")

elif days>365*2 and days<=365*3:
    print("3 st service interval")    

else:
    print("wrong time")
