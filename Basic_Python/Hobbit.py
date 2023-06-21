"""def bin(digit, n):
    arr = []
    for i in range(digit):
        arr.append(n % 2)
        n = n >> 1

    for i in range(digit - 1, -1, -1):
        print(arr[i], end="")

# function to generate all binary numbers of N digit.
def generateAllBin(n):
    high = int(pow(2, n))
    for i in range(high):
        bin(n, i)
        print()

n = int(input("Enter the number: "))

print("BINARY - ")
generateAllBin(n)"""

def generate_code_sequence(n):

    result = [0]

    binary = []
    for i in range(n):

        length = len(result)
        # Reverse the current sequence

        for j in range(length - 1, -1, -1):

            result.append(result[j] | (1 << i))
    for i in range(len(result)):

        binary_str = bin(result[i])[2:].zfill(n)

        binary.append(binary_str)

    print('DECIMAL -', result)

    print('BINARY -', binary)
    return result
n = 2

generate_code_sequence(n)