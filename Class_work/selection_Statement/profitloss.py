# Program to calculate profit or loss
# input cost price and selling price from the user

cost_price = float(input("Enter the cost price: "))
selling_price = float(input("Enter the selling price: "))
# calculating profit or loss

if selling_price > cost_price:
    profit = selling_price - cost_price
    print("Profit:", profit)
elif cost_price > selling_price:
    loss = cost_price - selling_price
    print("Loss:", loss)
else:
    print("No profit, no loss.")

'''Output:
Enter the cost price: 100
Enter the selling price: 150
Profit: 50.0
