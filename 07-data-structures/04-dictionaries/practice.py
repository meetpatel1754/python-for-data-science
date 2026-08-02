car = {
    "brand": "Honda",
    "model": "City",
    "year": 2023
}

print(car)

print(car["brand"])

car["color"] = "White"

car["year"] = 2024

print(car)

employee = {
    "id": 101,
    "name": "Meet",
    "salary": 50000
}

print(employee.keys())
print(employee.values())
print(employee.items())

employee.update({"department": "Data Science"})

employee.pop("salary")

print(employee)

students = {
    "Meet": 90,
    "Rahul": 85,
    "Priya": 95
}

for name, marks in students.items():
    print(name, "->", marks)