# Iterator in Python
list1 = [1, 4, 6, 'Raj', True]
l1_iter = iter(list1)

# print(next(l1_iter))
# print(next(l1_iter))
# print(next(l1_iter))
# print(next(l1_iter))
# print(next(l1_iter))
for i in l1_iter:
    print(i)


def generator1():
    print("Hello from Parkar")
    yield 5

    print("Hello from Pune")
    yield 10

    print("Hello from India")
    yield 15


generator_values = generator1()
# print(generator_values)
#
# print(next(generator_values))
# print(next(generator_values))
# print(next(generator_values))
for i in generator_values:
    print(i)