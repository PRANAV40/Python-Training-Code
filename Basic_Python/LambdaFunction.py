x = lambda a, b: a * b
print(x(4, 5))

d = lambda a: a + 20
print(d(30))

# Lambda with filter function
ages = [5, 7, 12, 18, 26, 28, 32]
adults = list(filter(lambda a: a > 18, ages))
print("Filter function: ", adults)

# Find the even number from a list using lambda function
number = [3, 5, 7, 11, 14, 16, 21, 18, 24, 17, 26, 28, 31]
even = list(filter(lambda a: a % 2 == 0, number))
print("Even number from the list using filter: ", even)

# Lambda function using map
number = [3, 5, 7, 11, 14, 16]
squares = list(map(lambda a: a * a, number))
print("Squares of number using map: ", squares)

# Lambda function using reduce
from functools import reduce
num = [1, 2, 3, 4, 5]
add = reduce(lambda a, b: a+b, num)
print(add)

# Find the maximum number in a list using reduce and lambda function
maximum = reduce(lambda a, b: a if a > b else b, num)
print(maximum)