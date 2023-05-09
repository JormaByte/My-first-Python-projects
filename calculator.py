print("Enter the first number:")
num_1 = int(input())

print("Enter the second number:")
num_2 = int(input())

print("Enter the operation:")
operation= input()

if operation == "+":
    print("The result is: " + str(num_1 + num_2))
elif operation == "-":
    print("The result is: " + str(num_1 - num_2))
elif operation == "/":
    print("The result is: " + str(num_1 / num_2))
elif operation == "*":
    print("The result is: " + str(num_1 * num_2))