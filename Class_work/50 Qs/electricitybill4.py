##Question 18: Calculate electricity bill based on units consumed.
##Input: Enter units
##Output: Total bill amount

## using while loop

units = int(input("Enter units consumed: "))

bill = 0

while units > 200:
    bill = bill + (units - 200) * 10
    units = 200

while units > 100:
    bill = bill + (units - 100) * 7
    units = 100

bill = bill + units * 5

print("Total bill amount:", bill)

'''
output

Enter units consumed: 100
Total bill amount: 500
'''