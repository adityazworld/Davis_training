##Question 3: Calculate electricity bill based on units consumed.
##Input: Enter units
##Output: Total bill amount       

units = int(input("Enter the number of units consumed: "))
if units <= 100:
    bill_amount = units * 0.5
elif units <= 200:
    bill_amount = 100 * 0.5 + (units - 100) * 0.75
elif units <= 300:
    bill_amount = 100 * 0.5 + 100 * 0.75 + (units - 200) * 1.20
else:
    bill_amount = 100 * 0.5 + 100 * 0.75 + 100 * 1.20 + (units - 300) * 1.50    

print("Total bill amount: Rs.", bill_amount)
'''Output:  
Enter the number of units consumed: 350
Total bill amount: Rs. 425.0
'''





