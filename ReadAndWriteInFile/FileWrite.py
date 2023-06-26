# "w" is write  in the file
f = open("FileWrite.txt", "w")
# "a" is append the content in the file
# f = open("FileWrite.txt", "a")
# If you check how many char in file then write like as following
char_in_file = f.write("Indentation refers to the spaces at the beginning of a code line.Where in other \n"
                       "programming languages the indentation in code is for readability only, the indentation\n"
                       "in Python is very important.Python uses indentation to indicate a block of code.")
print(char_in_file)
f.close()
