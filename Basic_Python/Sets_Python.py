my_sets = {10, "Parkar", 34.5, True}
print(my_sets)

# Create a empty set
# my_sets1 = set()
# print(type(my_sets))

# Add in the sets
my_sets.add(32)
print(my_sets)

my_sets.remove(10)
print(my_sets)
print(len(my_sets))

# Unioins on sets
print(my_sets)
my_sets1 = {"Laptop", 10, 67, 34.5}
print(my_sets1)
print(my_sets.union(my_sets1))
print(my_sets1 | my_sets)

# Update the set using given methods
print(my_sets)
my_sets.update(["Parkar", "Marks"])
print(my_sets)

# Intersection in python
print(my_sets1)
print(my_sets.intersection(my_sets1))
print(my_sets & my_sets1)

my_sets.intersection_update(my_sets1)
print(my_sets)
my_sets1.intersection_update(["Mohan", "Shiva"])
print(my_sets1)


# Difference between two sets
set1 = {"Ram", "Shyam", "Mani"}
set2 = {"Mani", "Jain", "Suresh"}
print(set1.difference(set2))
print(set1 - set2)
print(set2.difference(set1))

set2.difference_update(set1)
print(set1)
print(set2)

# Symmetrics difference of set
print(set1.symmetric_difference(set2))
# Symmetrics difference of set using operator and it work on more then two sets
print(set1 ^ set2)

# Update the symmetric differenece
set2.symmetric_difference_update(set1)
print(set2)
set1.symmetric_difference_update(('Mohan', 'Shiva'))
print(set1)
