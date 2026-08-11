# Exercise 1
# Create a class named Laptop.
class laptop:
    def __init__(self, brand, ram):
        self.brand = brand
        self.ram = ram

# Exercise 2
# Create two Laptop objects.
laptop1 = laptop("HP", "16gb")
laptop2 = laptop("DELL", "16gb")

# Exercise 3
# Add brand and RAM attributes.
laptop3 = laptop("Asus", "16gb")

# Exercise 4
# Print both attributes.
print(laptop1.brand)
print(laptop1.ram)

# Exercise 5
# Create a Mobile class and one object.
class mobile:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        print(self.brand,self.model)

mobile1 = mobile("vivo", "A17")
mobile1.info()

# Exercise 1
# Create a Person class with name and age.
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Exercise 2
# Create a method introduce().
    def introduce(self):
        print("Your Name is ",self.name)
        print("Your Age is ",self.age)

person1 = person("Meet","19")
person1.introduce()

# Exercise 3
# Create a Rectangle class with length and width.
class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

# Exercise 4
# Create a method area() that returns:
# length * width
    def area(self):
        return self.length * self.width
    
# Exercise 5
# Create two Rectangle objects and print their areas.
rectangle1 = rectangle(10,15)
rectangle2 = rectangle(50,75)
print("area : ",rectangle1.area())
print("area : ",rectangle2.area())