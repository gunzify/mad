try:
    num1 = float(input("Enter your first number: "))
except ValueError:
    print("Check your number well")

operand = input("Enter your operand (/,-,+,*): ")

try:
    num2 = float(input("Enter your second number: "))
except ValueError:
    print("Check your number well")

# Concatenate the operand within the expression
r = f"{num1} {operand} {num2}"

# Use eval to calculate the result
result = eval(r)

# Print the result
print(result)
