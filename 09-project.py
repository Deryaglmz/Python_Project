
names = ['Ali' , 'Yağmur','Hakan', 'Deniz',]
years = [1998, 2000, 1999, 1987]

names.append('Cenk')
names.insert(0, 'Sena')
names.insert(-1, 'Mehmet')
names.insert(len(names), 'Mehmet')

names.remove('Deniz')
names.pop()
names.pop(1)

index = names.index('Deniz')
print(index)

print(names)

index = names.index('Deniz')
names.pop(index)
print(names)

result = 'Ali' in names
result = names.index('Ali')
print(result)

names.reverse()
print(names)

names.sort()
print(names)

years.sort()
print(years)

######

list1 = ['Chevrolet','Dacia']
print(list1)

str = 'Chevrolet, Dacia'
result = str.split(',')
print(result)

result = max(years)
print(result)
result = min(years)
print(result)


print(years.count(1998))

years.clear()
print(years)

######

brands = []

brand = input("Brand: ")
brands.append(brand)

brand = input("Brand: ")
brands.append(brand)

brand = input("Brand: ")
brands.append(brand)

print(brands)



