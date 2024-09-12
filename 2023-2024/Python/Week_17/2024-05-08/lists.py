# christopher
# 2024-05-06

# creating an empty list
lst = []

# using a for loop to add number 1-100 to the list
for c in range(1,101):
    lst.append(c)

# printing the list lst
print(lst)

# create an empty list name odd
odd = []

# using a for loop to add number 1-100 to the list odd
for c in range(1,101,2):
    odd.append(c)

# printing the list odd
print(odd)

# create an empty list name even
even = []

# using a for loop to add number 1-100 to the list even
for c in range(2,101,2):
    even.append(c)

# printing the list even
print(even)

# create a variable maned b that points to the first list that you create
b = lst

# create a variable named joined that joines even and odd lists using a opperator
joined = even + odd

# output the varible joined
print(joined)

# output the type of the variadle joined
print(type(joined))

# compare the list b to the list joined using positional comparaion
print(b==joined)