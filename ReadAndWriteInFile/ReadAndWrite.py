# Handle read and write both in same program
f = open("FileWrite.txt", "r+")
print(f.read())

f.write("\nThank you Python")