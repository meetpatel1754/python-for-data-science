class Student:

    def __init__(self):
        print("Student object created")

student1 = Student()
student2 = Student()

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Meet", 20)

print(student1.name)
print(student1.age)

class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

student1 = Student("Meet", 20, "BCA")
student2 = Student("Rahul", 21, "B.Tech")

print(student1.name)
print(student2.course)