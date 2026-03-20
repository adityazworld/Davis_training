##Question 15: Create a function to calculate simple interest.
##Input: Enter P, R, T
##Output: Simple Interest


def simple_interest(p, r, t):
    one_percent = p / 100
    yearly_interest = one_percent * r
    total_interest = yearly_interest * t
    return total_interest

p = float(input("Enter Principal (P): "))
r = float(input("Enter Rate (R): "))
t = float(input("Enter Time (T): "))

print("Simple Interest:", simple_interest(p, r, t))

'''
output

Enter Principal (P): 100
Enter Rate (R): 10
Enter Time (T): 10
Simple Interest: 100.0
'''