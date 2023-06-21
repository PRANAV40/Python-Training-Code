# Program of Basic data type
var_1 = 4567
print(var_1)
print(type(var_1))

var_2 = 45.3e1
print(var_2)
print(type(var_2))

var_3 = 2 + 3j
print(var_3)
print(type(var_3))

var_4 = "I am from Parkar Global"
print(var_4)
print(type(var_4))

# Suppressing Special Character Meaning
# print('This string contains a single quote (') character.') It showing error because
# Specifying a backslash in front of the quote character in a string “escapes”
print('This string contains a single quote (\') character.')
# string delimited by double quotes
print("This string contains a double quote (\") character.")

# break up a string over more than one line, include a backslash before each newline
print('a\
... b\
... c')

# tab character can be specified by the escape sequence \t and for new line \n
print('Parkar\tGlobal')
print('Parkar\nGlobal')

# Triple-Quoted Strings
print('''This string has a single (') and a double (") quote.''')

# Boolean
a = 1
b = 2
var = a < b
varr = a > b
print(var)
print(type(var))
print(varr)
