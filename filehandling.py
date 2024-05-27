# Open a file

f = open("file.txt", "r")

if f.readable():
    print(f.read()) # Read the entire file
    print(f.readline()) # Read the first line
    
    for line in f.readlines(): # Read all lines as a list
        print(line)
        
f.close()

# Output: Hello, World! This is a file.

# Write to a file

f = open("file.txt", "w")

f.write("This is a file.")

f.close()

# Append to a file

f = open("file.txt", "a")

f.write(" This is an appended file.")

f.close()