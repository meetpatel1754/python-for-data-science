student = {
    "name": "Meet",
    "age": 20,
    "city": "Vadodara"
}

# Loop through keys
for key in student:
    print(key)

print("----------------")

# Loop through values
for value in student.values():
    print(value)

print("----------------")

# Loop through key-value pairs
for key, value in student.items():
    print(key, ":", value)