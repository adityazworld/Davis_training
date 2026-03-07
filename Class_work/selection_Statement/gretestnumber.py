#Writr a program to find the greatest  among 5 numbers

# Input 5 numbers from the user

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = float(input("Enter the third number: "))
number4 = float(input("Enter the fourth number: "))
number5 = float(input("Enter the fifth number: "))

# Find the greatest number
if(number1==number2) and (number1==number3) and (number1==number4) and (number1==number5):
    print("All numbers are equal.")

elif (number1 >= number2) and (number1 >= number3) and (number1 >= number4) and (number1 >= number5):
    print("The greatest number is:", number1)

elif (number2 >= number1) and (number2 >= number3) and (number2 >= number4) and (number2 >= number5):
    print("The greatest number is:", number2)

elif (number3 >= number1) and (number3 >= number2) and (number3 >= number4) and (number3 >= number5):
    print("The greatest number is:", number3)

elif (number4 >= number1) and (number4 >= number2) and (number4 >= number3) and (number4 >= number5):
    print("The greatest number is:", number4)

else:
    print("The greatest number is:", number5)

'''Output:
Enter the first number: 10
Enter the second number: 20
Enter the third number: 15
Enter the fourth number: 5
Enter the fifth number: 25
The greatest number is: 25.0
