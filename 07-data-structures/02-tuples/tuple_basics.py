# Creating Tuples
fruits = ("Apple", "Banana", "Mango", "Orange")
print(fruits)

# Creating a tuple with a single item
t1 = ("Hellow",)
print(t1)
print(type(t1))

# Same Data types (homogeneous)
t2 = (1,2,3,4)
print(t2)

# Different Data Types (hetrogeneous)
t3 = (10, 5.5, "Meet", True)
print(t3)

# 2D Tuple
t4 = (1,2,3,(4,5))
print(t4)

# Using Type Conversion 
t5 = tuple("Hello")
print(t5)

# Accessing Items
# - Indexing
# - Slicing

# Access Elements
print(fruits[0])
print(fruits[1])
print(fruits[-1])

# Slicing 
print(fruits[1:3])
print(fruits[::-1]) # reversing 
print(t4[-1][1])

# Editing Items
# t3[0] = 57
# Tuples are immutable like strings

# Adding Items 
# not possible because of tuples are immutable 

# Deleting items
del t2  # it will work
# del t2[-1]  <-  it will not work

# Operation on Tuples
# 1. + and *
t1 = (1,2,3,4)
t2 = (5,6,7,8)
print(t1 + t2)
print(t1 * 2)

# 2. Membership
print(1 in t1)

# 3. iteration
for i in t1:
    print(i)


# Tuple Functions
# len / sum / min / max / sorted
t = (1,2,3,4,5,6,7)
print(len(t))
print(sum(t))
print(min(t))
print(max(t))
print(sorted(t))
print(sorted(t, reverse=True))

# count
t = (1,3,5,7,4,3,5,2,7,6,8)
print(t.count(7))

# index
print(t.index(4))

# Special Syntax 
   
# Tuple Unpacking
a,b,c =(1,2,3)
print(a,b,c)

#Swap
a = 1
b =2
a,b = b,a 
print(a,b)

a,b,*other = (1,2,3,4)
print(a,b)
print(other)

# Zipping tuples
a = (1,2,3,4)
b = (5,6,7,8)

zip(a,b)
print(zip(a,b))

print(list(zip(a,b)))
print(tuple(zip(a,b)))