
# while

x = 0

while x < 100:
    print(x)
    x = x + 1

print('end...')    

########

x = 1

while x <= 100:
    print(x)
    x +=  1

print('end...')

#########

x = 1

while x <= 100:
    if x % 2==0:
      print(x)
    x +=  1

print('end...')

########

x = 1

while x <= 100:
    if x % 2==1:
      print(f'number odd: {x}')

    else:
       print(f'number even: {x}')  
    x +=  1

print('end...')

########

name = '' # False
while not name.strip():
   name = input('Name: ')

print(f'Hello, {name}')   

########

numbers = [1,3,5,9,12,19,21]

i = 0
while (i < len(numbers)):
    print(numbers[i])
    i += 1

########

beginning = int(input('beginning: ')) 
finish =  int(input('finish: ')) 

i = beginning
while i < finish:
    i += 1
    print(i)

########

beginning = int(input('beginning: ')) 
finish =  int(input('finish: ')) 

i = beginning
while i < finish:
    i += 1
    if (i % 2 == 1):
        print(i)

#########

i = 100

while i > 0:
    print(i)
    i -= 1

#########

numbers = []

i = 0

while i < 5:
    num = int(input('number: '))
    numbers.append(num)
    i += 1

numbers.sort()

print(numbers)

######

products = []

piece = int(input('how many products do you want to add'))  
i = 0

while(i<piece):
    name = input('product name: ')
    price = input('product name: ')
    products.append({
        'name' : name,
        'price' : price
    })
    i += 1

for procut in products:
    print(f'product name: {procut["name"]} product name: {procut["price"]}')    
