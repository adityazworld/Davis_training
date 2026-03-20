
##Question 2) Number Classification System 

def classify_num(num):
    
    if num > 0:
        return "Positive"
        # Nested if: Even or Odd (only meaningful for non-zero)
        if num % 2 == 0:
           return   "Even"
        else:
          return  "Odd"
    elif num < 0:
        return  "Negative"

        if num % 2 == 0:
            return"Even"
        else:
            return"Odd"

    else:
        return  "Zero"
        

## List of students
numbers = [12, -7, 0, 33, -44, 5, -2, 0, 19, 100]

print("=" * 45)
print(f"{'Number':>8}  {'Sign':<10}  {'Even / Odd':<10}")
print("=" * 45)

for num in numbers :
    sign =classify_num(num)
    parity = classify_num(num)

print(f"{num:>8}  {sign:<10}  {parity:<10}")
 
print("=" * 45)  