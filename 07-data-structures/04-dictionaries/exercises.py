# Exercise 1
# Create a dictionary for a book.
book = {
    "author" : "xyz",
    "pages" : 179,
    "title" : "abc",
    "year" : 2024
}
print(book)

# Exercise 2
# Print the author's name.
print(book["author"])

# Exercise 3
# Add the price.
book["price"] = "280"
print(book)

# Exercise 4
# Update the publication year.
book["year"] = 2025

# Exercise 5
# Print the total number of key-value pairs.
print(len(book))
print(book)

# Exercise 6
# Create a dictionary of a mobile phone.
phone = {
    "company" : "apple",
    "model" : "17",
    "price" : 117000,
    "Launch_year" : 2026
}

# Exercise 7
# Print all keys.
print(phone.keys())

# Exercise 8
# Print all values.
print(phone.values())

# Exercise 9
# Remove one key using pop().
phone.pop("Launch_year")
print(phone)

# Exercise 10
# Update the dictionary with a new key.
phone.update({"year" : 2026})
print(phone)

# Exercise 11
# Create a nested dictionary for two books.
books ={
    "book1" : {
        "name" : "abc",
        "author" : "xyz"
    },
    "book2" : {
        "name" : "mno",
        "author" : "ghi"
    }
}

# Exercise 12
# Print the author of the first book.
print(books["book1"]["author"])

# Exercise 13
# Loop through all keys.
for key in books.values():
    print(key.keys())

# Exercise 14
# Loop through all values.
for value in books.values():
    print(value.values())

# Exercise 15
# Loop through all key-value pairs.
for key, value in books.items():
    print(key, " : ",value)