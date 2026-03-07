# write the program to calculate simple interest and validate the input values

# taking input from the user
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))
# validating the input values
# calculating simple interest
simple_interest = (principal * rate * time) / 100
 #validating the simple interest
if simple_interest > 0:
    print("The simple interest is:", simple_interest)
else:
    print("Invalid input values. Simple interest cannot be calculated.")

'''Output:
Enter the principal amount: 1000
Enter the rate of interest: 5
Enter the time in years: 2
The simple interest is: 100.0