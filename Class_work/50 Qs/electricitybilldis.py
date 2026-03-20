##Question 8: Calculate electricity bill based on units consumed.
##Input: Enter units
##Output: Total bill amount
## using function

def electricity_bill(units):
    if units<=100:
        bill=units*10
    elif units<=200:
        bill=100*10+(units-100)*20
    else:
        bill=100*10+100*20+(units-200)*30
    return bill

##input

units=int(input("Enter the units: "))
print("Total bill amount is:",electricity_bill(units))

'''output
Enter the units: 100
Total bill amount is: 1000
'''