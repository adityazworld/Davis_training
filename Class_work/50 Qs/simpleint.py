##Question 5: Create a function to calculate simple interest.
##Input: Enter P, R, T
##Output: Simple Interest

##input 

p=float(input("Enter the principal: "))
r=float(input("Enter the rate: "))
t=float(input("Enter the time: "))

##formula
simple_interest=p*r*t/100

print("Simple interest is:",simple_interest)

'''output
Enter the principal: 100
Enter the rate: 10
Enter the time: 10
Simple interest is: 100.0
'''