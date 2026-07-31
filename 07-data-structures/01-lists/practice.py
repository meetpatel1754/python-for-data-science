student = ["Meet", 20, "BCA", "Vadodara"]

print(student)
print(student[0])
print(student[-1])
student[2] = "Data Science"
print(student)
print(len(student))

cities = ["Vadodara", "Ahmedabad"]
cities.append("Surat")
cities.insert(1, "Rajkot")
print(cities)
cities.remove("Ahmedabad")
print(cities)
cities.pop()
print(cities)

# List Comprehension
numbers = [10, 20, 30, 40, 50]

double = [num * 2 for num in numbers]
print(double)

odd = [num for num in numbers if num % 20 != 0]
print(odd)