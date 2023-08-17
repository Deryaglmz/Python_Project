
x , y, z = 2, 5 ,7 

numbers = 1, 5 , 7 ,10, 6

nuber1 = int(input("Please enter a number: "))
nuber2 = int(input("Please enter a number: "))

result = (nuber1*nuber2) - (x + y + z)

print(result)

#######

result = y // x
print(result) 

#######

total = (x + y + y)
result = total % 3
print(total)

#######

result = y**x
print(result)

#######

numbers = 1, 5 , 7 ,10, 6
x, *y , z = numbers
result = z ** 3
print(result)

#######

numbers = 1, 5 , 7 ,10, 6
x, *y , z = numbers
result = y[0] + y[1] + y[2]
print(result)
