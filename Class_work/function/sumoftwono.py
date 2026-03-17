##program to calculate sum of two numbers using function

#taking input from the user
num1 = float(input("Enter the frst value: "))
num2 = float(input("Enter the second value: "))
 
#defining a function to calculate the sum

def sum_of_two_no(num1 , num2):

    return num1 + num2

#calling the function and storing the result in a variable
result = sum_of_two_no(num1, num2)

#displaying the result


print("The sum of", num1, "and", num2, "is:", result)

'''Output:
Enter the frst value: 5 
Enter the second value: 10
The sum of 5.0 and 10.0 is: 15.0
'''