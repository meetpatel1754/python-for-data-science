# function for print *
def star():
    print("*")

star()

def hello(name):
    print("Hello",name)
hello("Meet")

def sum(a,b):
    print(a+b)
sum(10,4)

def intro(name, city):
    print("Name: ",name)
    print("City: ",city)
intro("Meet","Vadodara")

def cube(number):
    print(number*number*number)
cube(2)

def multiply(a, b):
    return a * b
result = multiply(5,7)
print(result)

country = "India"
def show_country():
    print(country)
show_country()

city = "Vadodara"
def info():
    age = 20
    print(city)
    print(age)
info()

# Create a lambda function that returns "Even" if the number is even, otherwise "Odd".
even_odd = lambda x : "Even" if x%2 == 0 else "odd"
print(even_odd(8))