
# for

numbers = [1,2,3,4,5]

for num in numbers:
    print(num)

########

numbers = [1,2,3,4,5]

for a in numbers:
    print('Hello')   

######## 

names = ['Abdullah' , 'Rıfkı', 'Şebelebettin']

for name in names:
    print(f'my name is {name}')

#########

name = 'Derya Gülmez'

for n in name:
    print(n)

#########

tuple = (1,2,3,4,5)  

for t in tuple:
    print(t)

##########

tuple = [(1,2), (1,3),(3,5),(5,7)]  

for t in tuple:
    print(t)

##########

tuple = [(1,2), (1,3),(3,5),(5,7)]  

for a,b in tuple:
    print(a)

#########

d = {'k1':1, 'k2':2, 'k3':3}   

for item in d:
    print(item)

####

d = {'k1':1, 'k2':2, 'k3':3}   

for item in d.items():
    print(item)

####

d = {'k1':1, 'k2':2, 'k3':3}   

for key, value in d.items():
    print(key)

#########

numbers = [1,3,5,7,9,12,19,21] 

for num in numbers:
    if(num%3==0):
        print(num) 
    
###

total = 0
for num in numbers:
    total = total + num
print(total)   

###

for num in numbers:
    if(num%2==1) :
        print(num **2) 

##########

cities = ['kocaeli', 'istanbul','ankara', 'izmir','rize']

for city in cities:
    if (len(city) <=5):
        print(city)

##########   

products = [
    {'name': 'samsung S6', 'price': '3000'},
    {'name': 'samsung S7', 'price': '4000'},
    {'name': 'samsung S8', 'price': '5000'},
    {'name': 'samsung S9', 'price': '6000'},
    {'name': 'samsung S10', 'price': '7000'},
]     

total = 0
for product in products:
    price = int(product['price'])
    total += price
print(total)    

###

for product in products:
    if (int(product['price']) <= 5000):
        print(product['name'])