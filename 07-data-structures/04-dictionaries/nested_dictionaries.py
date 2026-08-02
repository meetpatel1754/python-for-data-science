# Nested Dictionary
students = {
    "student1": {
        "name": "Meet",
        "age": 20,
        "course": "BCA"
    },
    "student2": {
        "name": "Rahul",
        "age": 21,
        "course": "B.Tech"
    }
}

print(students)

# Access Nested Values
print(students["student1"]["name"])
print(students["student2"]["course"])