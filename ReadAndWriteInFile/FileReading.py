f = open("FileRead.txt", "rt")
# It read all the content of the file
# contant = f.read()
# print(contant)

# It print a list of the contant
print(f.readlines(), end="")

# Read the file line by line
print(f.readline(), end="")
print(f.readline(), end="")

# Read the file line by line
# for line in f:
#     print(line,end="")
f.close()