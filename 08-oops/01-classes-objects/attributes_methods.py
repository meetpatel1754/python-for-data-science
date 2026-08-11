class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print("My name is", self.name)
        print("I am", self.age, "years old")
        print("I am studying", self.course)


student1 = Student("Meet", 20, "BCA")
student2 = Student("Ajay", 19, "BCom")

print(student1.name)
print(student1.age)

student1.introduce()
student2.introduce()