
# value types => string, number
x = 5
y = 25

x = y

y= 10

print(x,y)

#referance types =>

a = ["apple" ,"banana"]
b = ["apple" ,"banana"]

a = b
b[0] = "grape"

print(a,b)

######

# x = 5
# y = 10
# z = 20

x, y, z = 5, 10, 20

# x, y = y ,x

x += 5      # x = x + 5
x -= 5      # x = x - 5
x *= 5      # x = x * 5
x /= 5      # x = x / 5
x %= 5      # x = x % 5
x //= 5     # x = x // 5
x **= 5     # x = x ** 5

#print(x,y,z)

#######

values = 1, 2, 3

print(values)
print(type(values))

x , y, z = values
print(x,y,z)

#######

values = 1, 2, 3, 4, 5

print(values)
print(type(values))

x , y, *z = values   # z = list 
print(x,y,z)
print(x,y,z[0])
