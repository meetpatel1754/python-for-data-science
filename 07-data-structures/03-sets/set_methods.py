fruits = {"Apple", "Banana", "Mango"}

# Add
fruits.add("Orange")
print(fruits)

# Remove
fruits.remove("Banana")
print(fruits)

# Discard
fruits.discard("Grapes")
print(fruits)

# Pop
item = fruits.pop()
print(item)
print(fruits)

# Clear
copy_set = fruits.copy()
copy_set.clear()
print(copy_set)