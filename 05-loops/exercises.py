# Exercise 1
# Print numbers from 1 to 25.
for i in range(1,26):
    print(i)
print("\n")

# Exercise 2
# Print only even numbers.
for i in range(0,10,2):
    print(i)
print("\n")

# Exercise 3
# Print only odd numbers.
for i in range(1,10,2):
    print(i)
print("\n")

# Exercise 4
# Find the sum of numbers from 1 to 100.
print("\n")
sum = 0
for i in range(1,101):
    sum += i
print(sum)
print("\n")

# Exercise 5
# Print multiplication table of any number.
print("\n")
for i in range(5,51,5):
    print(i)
print("\n")

# Exercise 6
# Print a star pattern.
for i in range(5):
    for j in range(i):
        print("*",end="")
    print(" ")
print("\n")

# Exercise 7
# Skip number 25 using continue.
for i in range(1,31):
    if i==25:
        continue
print("\n")

# Exercise 8
# Stop the loop when number becomes 50 using break.
for i in range(1,60):
    if i==50:
        break