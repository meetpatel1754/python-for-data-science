student = {
    "name": "Meet",
    "age": 20,
    "course": "BCA"
}

# keys()
print(student.keys())

# values()
print(student.values())

# items()
print(student.items())

# get()
print(student.get("name"))
print(student.get("city"))  # Returns None

# pop()
student.pop("course")
print(student)

# update()
student.update({"city": "Vadodara"})
print(student)

# popitem()
student.popitem()
print(student)

# clear()
temp = student.copy()
temp.clear()
print(temp)