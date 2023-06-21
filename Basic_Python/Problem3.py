'''
Problem3:
Create a function that takes a list of non-negative integers and strings and return a new list without the strings.
Examples
filter_list([1, 2, "a", "b"]) ➞ [1, 2]
filter_list([1, "a", "b", 0, 15]) ➞ [1, 0, 15]
filter_list([1, 2, "aasf", "1", "123", 123]) ➞ [1, 2, 123]
'''
input_list = [1, 2, "a", "b"]


def filter_string_lists(lists):
    new_list = []
    for i in input_list:
        if type(i) == int:
            new_list.append(i)
    return new_list


print(filter_string_lists(input_list))



# return [num for num in lists if isinstance(num, int)]
# filtered_new_list = filter_string_lists(input_list)
# print(filtered_new_list)
