num = int(input("Enter frist range of number: "))
num1 = int(input("Enter second range of number: "))
for i in range(num, num1):
    if i % 7 == 0 and i % 5 != 0:
        print(i, end=',')


# Reverse the int number
'''num = int(input("Enter the number: "))
print("The number before reverse: ", num)
reverse = 0
while num != 0:
    reverse = reverse * 10 + num % 10
    num = num // 10
print("After reverse the number is: ", reverse)'''


'''# Number fabinoci series
num = int(input("Enter the number: "))
first, second = 0, 1
print("Fibonacci series are : ", end="")
for i in range(0, num):
    if i <= 1:
        result = i
    else:
      result = first + second
      first = second
      second = result
    print(result, end=" ")'''