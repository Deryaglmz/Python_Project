
# if 
if 3==3:        #3>2 True
    print("Hello World")

if True:        
    print("Hello World")    

if False:       
    print("Hello World")    

#########

isLoggedin = True

if isLoggedin:
    print("welcome") 

#########

isLoggedin = False

if isLoggedin:
    print("welcome") 

#########

username = 'sadikturan'
password = '1234'

isLoggedin = (username == 'sadikturan') and (password == '1234')

if isLoggedin:
    print("welcome") 

########   

username = 'sadikturan'
password = '1234'

if (username == 'sadikturan') and (password == '1234'):
    print("welcome") 

########

username = 'sadikturan'
password = '1234'

if (username == 'sadikturan') and (password == '1234'):

    print("welcome") 

else :
    print("username or password false")

########    

username = 'sadikturan'
password = '1234'

if (username == 'sadikturan') :
    if (password == '1234'):
        print("welcome") 

    else:
        print("passworld false")    
    
else:
    print("username false")

#########

# elif

x = 10
y = 20

if x > y:
    print("x more than y")
else:
    print("y more than x")    

########

x = 20
y = 20

if x > y:
    print("x more than y")

elif x == y:
    print("x y equal") 

else:
    print("y more than x") 

########

x = int(input('x: '))
y = int(input('y: '))

if x > y:
    print("x more than y")

elif x == y:
    print("x y equal") 

else:
    print("y more than x") 

#########

num = int(input('number: '))

if num > 0:
    print("number positive")

elif num < 0:
    print("number negative")  

else :
    print('number zero')      
    