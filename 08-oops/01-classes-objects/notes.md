# Classes and Objects

## Class
A class is a blueprint for creating objects.

## Object
An object is an instance of a class.

## Syntax
```python
class Student:
    pass

student = Student()
```

## Attributes
Attributes store data.
Example
```python
student.name = "Meet"
student.age = 20
```

## Constructor
A constructor is a special method that is called automatically when an object is created.

Syntax
```python
def __init__(self):
    ...
```

## self
`self` refers to the current object.

## Attributes
Attributes store data belonging to an object.

Example:
self.name = name

## Methods
Methods are functions defined inside a class.

Example:
def introduce(self):
    print(self.name)

## Difference
Attribute → Data/Property
Method → Action/Behavior