#Question 13: Calculate electricity bill based on units consumed.
#Input: Enter units
#Output: Total bill amount

units = int(input("Enter units consumed: "))

bill = 0

if units > 200:
    bill = bill + (units - 200) * 10
    units = 200

if units > 100:
    bill = bill + (units - 100) * 7
    units = 100

bill = bill + units * 5

print("Total bill amount:", bill)

'''
output

Enter units consumed: 100
Total bill amount: 500
'''