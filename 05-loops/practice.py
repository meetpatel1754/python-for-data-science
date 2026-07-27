# Print your name 10 times
for i in range(10):
    print("Meet")

# Print numbers from 1 to 20
for i in range(1,21):
    print(i)

# Print even numbers from 2 to 20
for i in range(1,21):
    if i%2 == 0:
        print(i)

# Print odd numbers from 1 to 19
for i in range(1,21):
    if i%2 != 0:
        print(i)

# Print square of numbers from 1 to 10
for i in range(1,11):
    print(i**2)

# Print numbers 1 to 10 using while loop
count = 1
while count < 10:
    print(count)
    count += 1

# Print numbers 10 to 1 using while loop
count = 10
while count >= 1:
    print(count)
    count -= 1

print("\n")
for i in range(7,71,7):
    print(i)

# Find the sum of numbers from 1 to 100.
print("\n")
sum = 0
for i in range(1,101):
    sum += i
print(sum)