# # This is list comprehension
# list_comp = [i for i in range(200, 320) if i % 7 == 0 and i % 5 != 0]
# print(list_comp)
# # This is dict comprehension
# dict1 = {i:f"Item {i}" for i in range(1, 10)}
# dict2 = {value:key for key, value in dict1.items()}
# print(dict1)
# print(dict2)


no_of_list = int(input("How many item you want to add: "))
input_string = input("Enter a list element separated by space:")
lists = input_string.split()
t = int(input("Which type of comprehension you use 1. List Comprehension "
              "2.Dictionary Comprehension 3. Set Comprehension "))

if t == 1:
    ls = [i for i in list]
    print(ls)
    print(type(ls))
elif t == 2:
    dict1 = {f'item{i}': i for i in list}
    print(dict1)
    print(type(dict1))
elif t == 3:
    s = {i for i in list}
    print(s)
    print(type(s))
else:
    print("Exit")
