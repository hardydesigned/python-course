# itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators
# The module standardizes a core set of fast, memory efficient tools that are useful by themselves or in combination.

from itertools import product, permutations, combinations, accumulate, groupby, count, cycle, repeat

# product

a = [1, 2]
b = [3, 4]
prod = product(a, b)
print(list(prod))  # [(1, 3), (1, 4), (2, 3), (2, 4)]

# permutations

a = [1, 2, 3]
perm = permutations(a)
print(list(perm))  # [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

# combinations

a = [1, 2, 3, 4]
comb = combinations(a, 2)
print(list(comb))  # [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

# accumulate
a = [1, 2, 3, 4]
acc = accumulate(a)
print(a)  # [1, 2, 3, 4]
print(list(acc))  # [1, 3, 6, 10]

# groupby
def smaller_than_3(x):
    return x < 3

a = [1, 2, 3, 4]
group_obj = groupby(a, key=smaller_than_3)
for key, value in group_obj:
    print(key, list(value)) # True [1, 2] False [3, 4]

# count
for i in count(10):
    print(i)
    if i == 15:
        break # 10 to 15

# cycle
a = [1, 2, 3]
for i in cycle(a):
    print(i)
    if i == 3:
        break # 1 to 3

# repeat
for i in repeat(1, 4):
    print(i)

# Output: [(1, 3), (1, 4), (2, 3), (2, 4)]