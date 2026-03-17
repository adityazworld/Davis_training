## write a program to check a number is odd or even using function

#taking input from the user

num = int(input("Enter a number: "))

#defining a function to check odd or even

def check_odd_even(num):
    
    if num % 2 == 0:
        return "Even"
    else:

        return "Odd"
    
#calling the function and storing the result in a variable

result = check_odd_even(num)

#displaying the result
print("The number", num, "is", result)
'''Output:
Enter a number: 7
The number 7 is Odd
'''
