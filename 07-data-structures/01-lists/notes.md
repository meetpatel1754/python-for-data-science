# Lists
A list is an ordered and mutable collection in Python.

## Features
- Ordered
- Mutable
- Allows duplicate values
- Can store multiple data types

## Creating a List
```python
fruits = ["Apple", "Banana", "Mango"]
```

## Indexing
```python
fruits[0]
fruits[-1]
```

## Slicing
```python
fruits[1:3]
fruits[:2]
fruits[2:]
fruits[::-1]
```

## Updating
```python
fruits[0] = "Orange"
```

## Common List Methods
append(x)  -> Add element at the end
insert(i, x) -> Insert at a specific index
remove(x) -> Remove the first matching element
pop() -> Remove the last element
extend(list) -> Add multiple elements
sort() -> Sort the list
reverse() -> Reverse the list
index(x) -> Return the index of an element
count(x) -> Count occurrences of an element
clear() -> Remove all elements

## List Comprehension
List comprehension is a shorter way to create a list.
Syntax
new_list = [expression for item in iterable]
With Condition
new_list = [expression for item in iterable if condition]
Examples
squares = [x*x for x in numbers]
evens = [x for x in numbers if x % 2 == 0]