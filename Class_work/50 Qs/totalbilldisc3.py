##Question 16: A shopkeeper wants to calculate total bill after discount.
##Input: Enter price and discount percentage
##Output: Final price after discount

def calculate_bill(price, discount):
    if discount < 0 or discount > 100:
        return "Invalid discount"
    
    discount_amount = (price * discount) / 100
    return price - discount_amount

price = float(input("Enter price: "))
discount = float(input("Enter discount %: "))

print("Final price =", calculate_bill(price, discount))

'''
output

Enter price: 100
Enter discount %: 10
Final price = 90.0
'''