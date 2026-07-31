cities = {"Vadodara", "Ahmedabad", "Surat"}

cities.add("Rajkot")
print(cities)

cities.remove("Surat")
print(cities)

print(len(cities))

python = {"Python", "SQL", "Pandas"}
skills = {"Python", "SQL", "Excel"}

print(python.union(skills))
print(python.intersection(skills))
print(python.difference(skills))