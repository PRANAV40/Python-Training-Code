my_list = [1, 2, 3, 4, 5]
print(my_list)
my_list[0] = 12
print(my_list)
my_list.sort()
print(my_list)

my_list1 = [4, 8, 2, 7, 9]

my_list.extend(my_list1)
my_list.sort()
print(my_list)

my_list2 = [11, 21, 31, 41]
my_list.append(my_list2)
print(my_list)

my_list.insert(3, 45)
print(my_list)

my_list.remove(45)
print(my_list)

print(my_list.pop())
print(my_list)

print(my_list.count(2))

my_list.copy()
print(my_list)

my_list.reverse()
print(my_list)

my_list.clear()
print(my_list)
