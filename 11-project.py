
# Dictionary
# key - value

cities = ['kocaeli', 'istanbul']
plates = [41, 34]

print(plates[cities.index('kocaeli')])

#print(plates['kocaeli'])  => 41
#print(plates['istanbul'])  => 34

plates = {'kocaeli' : 41, 'istanbul' : 34}

print(plates['kocaeli']) 
print(plates['istanbul']) 

plates['ankara'] = 6
plates['kocaeli'] = 'new value'
print(plates)

#######

users = {
    'derya' : {
        'age' : 20 ,
        'email' : 'derya@gmail.com' ,
        'roles' : ['user'] ,
        'adress': 'istanbul',
        'phone' : '123432'
    },

    'pelin' :{
        'age' : 19 ,
        'email' : 'pelin@gmail.com' ,
        'roles' : ['user' ,'admin'] ,
        'adress': 'istanbul',
        'phone' : '545442'
    }
}

#print(users['pelin'])
#print(users['pelin']['age'])
#print(users['pelin']['email'])
#print(users['pelin']['adress'])

print(users['pelin']['roles'])
print(users['pelin']['roles'][0])
