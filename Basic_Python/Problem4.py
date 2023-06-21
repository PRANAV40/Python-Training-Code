'''
Problem 4:
Write a program (using functions!) that asks the user for a long string containing multiple words. Print back
to the user the same string, except with the words in backwards order. For example, say I type the string:
 My name is Michele
Then I would see the string:
 Michele is name My
'''

input_string = input("Enter the string: ")


def reverse_string(self):
    long_string = input_string.split()
    long_string.reverse()
    print(" ".join(long_string))

reverse_string(input_string)