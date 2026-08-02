# Dictionaries
A dictionary stores data in **key-value pairs**.

## Features
- Mutable
- Ordered (Python 3.7+)
- Keys must be unique
- Fast lookup using keys

## Syntax
```python
student = {
    "name": "Meet",
    "age": 20
}
```

## Access
```python
student["name"]

student.get("name")
```

## Add
```python
student["city"] = "Vadodara"
```

## Update
```python
student["age"] = 21
``` 

## Dictionary Methods
### keys()
Returns all keys.

```python
student.keys()
```

### values()
Returns all values.

```python
student.values()
```

### items()
Returns key-value pairs.

```python
student.items()
```

### get()
Safely returns a value.

```python
student.get("name")
```

### pop()
Removes a specific key.

```python
student.pop("age")
```

### popitem()
Removes the last inserted key-value pair.

### update()
Updates or adds key-value pairs.

```python
student.update({"city": "Vadodara"})
```

### clear()
Removes all items.

## Nested Dictionaries
A dictionary can contain another dictionary as its value.

Example
```python
students = {
    "student1": {
        "name": "Meet",
        "age": 20
    }
}
```

Access

```python
students["student1"]["name"]
```

## Looping
Keys

```python
for key in student:
```

Values

```python
for value in student.values():
```

Key-Value

```python
for key, value in student.items():
```