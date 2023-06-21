from collections import OrderedDict
# Dict in Python
my_dicts = {"Name": "Raj", "Course": "BCA", "Age": 21}
print(my_dicts)
print(type(my_dicts))
print(my_dicts.keys())
print(my_dicts.values())
print(my_dicts.items())

my_dict = {}
my_dict['a'] = 1
my_dict['b'] = 2
my_dict['c'] = 3
my_dict['d'] = 4
my_dict['e'] = 5
my_dict['f'] = 6
print(my_dict)
print(type(my_dict))

oder_dict = OrderedDict()
oder_dict['a'] = 1
oder_dict['a'] = 1
oder_dict['b'] = 2
oder_dict['c'] = 3
oder_dict['d'] = 4
oder_dict['e'] = 5
print(oder_dict)
print(type(oder_dict))

add = lambda num: num + 4
print(add(6))

# OrderedDict in Python
numbers = OrderedDict([("One", 1), ("Two", 2), ("Three", 3)])
print(numbers)

letters = OrderedDict({("a", 1), ("b", 2), ("c", 3)})
print(letters)

numbers = OrderedDict({"One": 1, "Two": 2, "Three": 3})
print(numbers)

numbers = OrderedDict(one=1, two=2, three=3)
print(numbers)

keys = ["one", "two", "three"]
print(OrderedDict.fromkeys(keys, 1))


numberss = OrderedDict(one=1, two=2, three=3)
print(numberss)

numberss["four"] = 4
print(numberss)

del numberss["one"]
print(numberss)

numberss["one"] = 1
print(numberss)


numbers = OrderedDict(one=1, two=2, three=3)
print(numbers)

numbers["one"] = 1.0
print(numbers)

numbers.update(two=2.0)
print(numbers)

print("This is itretor using keys numbers directly")
numbers = OrderedDict(one=1, two=2, three=3)
for key in numbers:
    print(key, "->", numbers[key])

print("This is itretor using items")
for key, value in numbers.items():
    print(key, "->", value)

print("This is itretor using keys")
for key in numbers.keys():
    print(key, "->", numbers[key])

print("This is itretor over values")
for value in numbers.values():
    print(value)

print("This is for reversed the order of Dict using keys numbers")
for key in reversed(numbers):
    print(key, "->", numbers[key])


print("This is for reversed the order of Dict using items")
for key, value in reversed(numbers.items()):
    print(key, "->", value)

print("This is for reversed the order of Dict using keys")
for key in reversed(numbers.keys()):
    print(key, "->", numbers[key])

print("This is for reversed the order of Dict using values")
for value in reversed(numbers.values()):
    print(value)

print(numbers)
numbers.move_to_end("one")
print(numbers)

numbers.move_to_end("one", last=False)
print(numbers)

print("Sorting the dict by keys ")
letterss = OrderedDict(b=2, c=3, e=5, d=4, a=1)
for key in sorted(letterss):
    letterss.move_to_end(key)
    print(letterss)

print("Sorting the dict by value")
letter = OrderedDict(d=5, a=3, b=1, c=2, e=4)
for key, _ in sorted(letter.items(), key=lambda item: item[1]):
    letter.move_to_end(key)
    print(letter)
