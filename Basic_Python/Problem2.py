'''
Problem2:
Create a function that takes a string and returns the number (count) of vowels contained within it.
Examples
count_vowels("Celebration") ➞ 5
count_vowels("Palm") ➞ 1
count_vowels("Prediction") ➞ 4
'''
strings_input = input("Enter the strings: ")


def strings_vowels(strings):
    count = 0
    vowels = "aeiouAEIOU"

    for i in strings:
        if i in vowels:
            count = count + 1
    print('count_vowels("', strings, '")->', count)


strings_vowels(strings_input)
