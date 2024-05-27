#Sets
#Sets are used to store multiple items in a single variable.
#A set is a collection which is unordered and unindexed.
#Sets are written with curly brackets.
#Sets are mutable, meaning they can be changed after they are created.

myset = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(myset)

myset1 = set(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

u = myset.union(myset1) # Union of two sets
print(u)

i = myset.intersection(myset1) # Intersection of two sets
print(i)

d = myset.difference(myset1) # Difference of two sets
print(d)

print(d.issubset(myset)) # Check if set is subset of another set
print(d.issuperset(myset1)) # Check if set is superset of another set
print(d.isdisjoint(myset1)) # Check if set has no elements in common with another set

cd = set.copy(myset) # Copy set

f = frozenset(myset) # Create immutable set