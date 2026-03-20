## Question 3) Multiplication Table Generator

def generate_table(n):
    print(f"\nMultiplication Table for {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

num = int(input("Enter a number to generate its multiplication table: "))
generate_table(num)
