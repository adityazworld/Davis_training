# program to calculate simple interest
# taking input from the user
principal = float(input("Enter principal(in rs): "))    

#validating the principal
if principal < 0:
    exit("Error: Principal amount cannot be negative.")
rate = float(input("Enter rate of interest(in %): "))
# validating the rate of interest
if rate < 0:
    exit("Error: Rate of interest cannot be negative.")
time = float(input("Enter time(in years): "))

# validating the time
if time < 0:
    exit("Error: Time cannot be negative.")
# calculating simple interest
simple_interest = (principal * rate * time) / 100

# displaying the result
print("The simple interest is:", simple_interest)


'''Output:
Enter principal(in rs): 1000
Enter rate of interest(in %): 5
Enter time(in years): 2 