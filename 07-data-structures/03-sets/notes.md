# Sets
A set is an unordered collection of unique elements.

## Features
- Unordered
- Mutable
- No duplicate values
- No indexing

Example
```python
fruits = {"Apple", "Banana", "Mango"}
```

## Common Methods
add(x)
remove(x)
discard(x)
pop()
clear()
copy()

## Important
Duplicate values are automatically removed.

Example
```python
numbers = {1, 2, 2, 3, 1}
print(numbers)

# Output
{1, 2, 3}
```

## Set Operations

### Union
Combines both sets.

```python
A | B
```

### Intersection
Common elements.

```python
A & B
```

### Difference
Elements present in first set only.

```python
A - B
```

### Symmetric Difference
Elements present in either set but not both.

```python
A ^ B
```

### Subset
```python
A.issubset(B)
```

### Superset
```python
B.issuperset(A)
```