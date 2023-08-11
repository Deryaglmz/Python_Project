
numbers = [1, 10, 5 , 16, 4 ,9 ,10]
letters = ['a', 'g', 's','b','y','a','s']

value = min(numbers)
value = max(numbers)
value = max(letters)
value = min(letters)

value = numbers[3:6]
value = numbers[:3]
value = numbers[4:]

numbers[4] = 40

numbers.append(49)
numbers.append(59)
numbers.insert(3,78)
numbers.insert(-1 ,20)

#numbers.pop()
#numbers.pop(0)
#numbers.pop(-1)

#numbers.remove(49)
#numbers.remove(40)

numbers.sort()
numbers.reverse()

letters.sort()
letters.reverse()

print(letters)
print(numbers)

print(len(numbers))
print(len(letters))

numbers.clear()

print(numbers.count(10))
print(letters.count('a'))