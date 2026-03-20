##question 7)

def atm():
    balance = 10000

    while True:
        print("\n1. Withdraw\n2. Exit")
        choice =int(input("Enter choice: "))

        if choice == 2:
            print("Thank you!")
            break

        amount = float(input("Enter withdrawal amount: "))

        if amount < 0:
            print("Invalid amount")
        elif amount > balance:
            print("Insufficient balance")
        else:
            balance -= amount
            print(f"Withdrawal successful. Remaining balance: {balance}")

atm()