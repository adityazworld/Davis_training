#Question 12: Check whether a person is eligible to vote.
#Input: Enter age
#Output: Eligible / Not Eligible

## Enter age

age = int(input("Enter your age: "))

check = age - 18

if check >= 0:
    print("Eligible")
else:
    print("Not Eligible")

'''
output

Enter your age: 18
Eligible
'''