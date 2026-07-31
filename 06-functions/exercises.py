# Exercise 1
# Create a function that prints your name.
def name():
    print("Meet")
name()

# Exercise 2
# Create a function that prints your city.
def city():
    print("Vadodara")
city()

# Exercise 3
# Call the same function 10 times.
def star():
    print("*")
for i in range(10):
    star()

# Exercise 4
# Create a function that accepts two numbers and prints their multiplication.
def multi(a, b):
    print(a*b)
multi(6,5)

# Exercise 5
# Return the larger of two numbers.
def large(a, b):
    if a > b:
        return a
    else:
        return b
largest = large(5, 9)
print(largest)

# Exercise 6
# Create one global variable and print it inside a function.
name = "Meet"
def greet():
    print("Hello",name)
greet()

# Exercise 7
# Create a lambda function to return the larger number.
large = lambda a, b: a if a > b else b
print(large(77,45))

