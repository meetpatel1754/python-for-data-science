fruits = ["Apple", "Banana", "Mango"]
print(fruits)

# append()
fruits.append("Orange")
print("append():", fruits)

# insert()
fruits.insert(1, "Grapes")
print("insert():", fruits)

# remove()
fruits.remove("Banana")
print("remove():", fruits)

# pop()
fruits.pop()
print("pop():", fruits)

# extend()
fruits.extend(["Kiwi", "Pineapple"])
print("extend():", fruits)

# sort()
numbers = [50, 20, 10, 40, 30]
numbers.sort()
print("sort():", numbers)

# reverse()
numbers.reverse()
print("reverse():", numbers)

# index()
print("Index of 40:", numbers.index(40))

# count()
values = [1, 2, 2, 3, 2, 4]
print("Count of 2:", values.count(2))

# clear()
values.clear()
print("clear():", values)