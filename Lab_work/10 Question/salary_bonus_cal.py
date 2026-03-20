## question 6)

def calculate_bonus(salary, experience):
    if experience >= 10:
        bonus = salary * 0.20
    elif experience >= 5:
        bonus = salary * 0.10
    else:
        bonus = salary * 0.05
    return bonus


n = int(input("Enter number of employees: "))

for i in range(1, n+1):
    salary = float(input(f"Enter salary of employee {i}: "))
    exp = int(input(f"Enter experience of employee {i}: "))
    
    bonus = calculate_bonus(salary, exp)
    print(f"Employee {i} Bonus: {bonus}")