# Creating Dictionary

student = {
    "name": "Meet",
    "age": 20,
    "course": "BCA"
}

print(student)

# Access Values
print(student["name"])
print(student["age"])

# Using get()
print(student.get("course"))

# Length
print(len(student))

# Different Data Types
person = {
    "name": "Meet",
    "age": 20,
    "height": 5.8,
    "is_student": True
}

print(person)

student = {
    "name": "Meet",
    "age": 20
}

# Add
student["city"] = "Vadodara"
print(student)

# Update
student["age"] = 21
print(student)