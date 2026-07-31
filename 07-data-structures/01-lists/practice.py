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