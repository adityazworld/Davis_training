##Question 7: Check whether a person is eligible to vote.
##Input: Enter age
##Output: Eligible / Not Eligible
## using function

def eligible_for_vote(age):
    if age >= 18:
        return "Eligible to vote"
    else:
        return "Not eligible to vote"

##input

age = int(input("Enter the age: "))
print(eligible_for_vote(age))

'''output
Enter the age: 18
Eligible to vote
'''