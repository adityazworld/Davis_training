
##Question 2) Number Classification System 

def classify_num(num):
    if num > 0:
        sign = "Positive"
        parity = "Even" if num % 2 == 0 else "Odd"
    elif num < 0:
        sign = "Negative"
        parity = "Even" if num % 2 == 0 else "Odd"
    else:
        sign = "Zero"
        parity = "N/A"
    return sign, parity

## List of numbers
numbers = [12, -7, 0, 33, -44, 5, -2, 0, 19, 100]

print("=" * 45)
print(f"{'Number':>8}  {'Sign':<10}  {'Even / Odd':<10}")
print("=" * 45)

for num in numbers:
    sign, parity = classify_num(num)
    print(f"{num:>8}  {sign:<10}  {parity:<10}")
 
print("=" * 45)