#While Loop

i = 1
while i <= 5:
    print(i)
    i += 1

#For Loop

for i in range(1, 6):
    print(i)

for i in "Giraffe":
    print(i)

for i in [1, 2, 3, 4, 5]:
    print(i)

#Nested Loop

for i in range(1, 4):
    for j in range(1, 4):
        print(f'i = {i}, j = {j}')