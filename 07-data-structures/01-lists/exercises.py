# Exercise 1
# Create a list of 5 favorite games.
games = ['cricket','football','chess','bedmiton','basball']
print(games)

# Exercise 2
# Print the first and last element.
print(games[0])
print(games[1])

# Exercise 3
# Replace the second element.
games[1] = 'hocky'
print(games)

# Exercise 4
# Print the length of the list.
print(len(games))

# Exercise 5
# Create a nested list with 3 rows.
n = [[0, 0],
     [0, 1],
     [0, 2]]
print(n)

# Exercise 6
# Create a list of 5 fruits and use append().
fruits = ['Banana', 'Apple', 'Mango']
fruits.append('Orange')
print(fruits)

# Exercise 7
# Insert your favorite city at index 1.
city = ['Amadavas', 'Surat']
city.insert(1, 'Vadodara')
print(city)

# Exercise 8
# Remove one fruit from the list.
fruits.remove('Mango')
print(fruits)

# Exercise 9
# Sort the numbers [5, 2, 9, 1, 7].
numbers = [20, 10, 60, 30, 50, 40]
numbers.sort()
print(numbers)

# Exercise 10
# Count how many times 10 appears in
# [10, 20, 10, 30, 10].
n = [10, 20, 10, 30, 10]
print(n.count(10))

# Exercise 11
# Create a list of squares from 1 to 10.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [num * num for num in numbers]

print(squares)

# Exercise 12
# Create a list of cubes from 1 to 5.
numbers = [1, 2, 3, 4, 5]
cubes = [number ** 3 for number in numbers]
print(cubes)

# Exercise 13
# Create a list of even numbers from 1 to 20.
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,20]
even = [n for n in num if n%2 == 0]
print(even)

# Exercise 14
# Convert all names to uppercase.
city = ['Vadodara', 'Surat', 'Amdavad']
uppercase = [c.upper() for c in city]
print(uppercase)

# Exercise 15
# Create a list of numbers greater than 50.
numbers = [20, 30, 40, 50, 60, 70, 80]
gretter_50 = [num for num in numbers if num > 50]
print(gretter_50)