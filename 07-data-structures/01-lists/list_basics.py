# Creating Lists
fruits = ["Apple", "Banana", "Mango"]
print(fruits)

# List with different data types
data = ["Meet", 20, 5.8, True]
print(data)

# Empty List
empty_list = []
print(empty_list)

# Length of List
print(len(fruits))

# Accessing Elements
print(fruits[0])
print(fruits[1])
print(fruits[2])

# Negative Indexing
print(fruits[-1])
print(fruits[-2])


# 📖 Indexing
numbers = [10, 20, 30, 40, 50]
print(numbers[0])
print(numbers[2])

print(numbers[-1])
print(numbers[-3])

# 📖 Slicing
print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[:])
print(numbers[::-1])

# 📖 Updating List
fruits[1] = "Orange"
print(fruits)

# 📖 Nested List
matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]
print(matrix)
print(matrix[0])
print(matrix[1][1])
print(matrix[2][0])