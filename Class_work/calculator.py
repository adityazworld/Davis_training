

## Clculator using switch case
def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        return "Invalid operator"
# taking input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")
result = calculator(num1, num2, operator)
print("The result of", num1, operator, num2, "is", result)

'''
Output:
Enter first number: 10
Enter second number: 5
Enter operator (+, -, *, /): +
The result of 10.0 + 5.0 is 15.0
Enter first number: 10
Enter second number: 5
Enter operator (+, -, *, /): -
The result of 10.0 - 5.0 is 5.0
Enter first number: 10
Enter second number: 5
Enter operator (+, -, *, /): *
The result of 10.0 * 5.0 is 50.0
Enter first number: 10
Enter second number: 5
Enter operator (+, -, *, /): /
The result of 10.0 / 5.0 is 2.0