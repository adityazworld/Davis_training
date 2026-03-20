##Question 19: Print all even numbers between 1 to N.
##Input: Enter N
##Output: Even numbers list

## using while loop

n = int(input("Enter N: "))

i = 2
while i <= n:
    print(i, end=" ")
    i = i + 2

'''
output

Enter N: 10
2 4 6 8 10 
'''