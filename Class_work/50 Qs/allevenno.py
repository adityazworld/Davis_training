##Question 9: Print all even numbers between 1 to N.
##Input: Enter N
##Output: Even numbers list
## using function

def even_numbers(n):
    for i in range(1, n+1):
        if i%2==0:
            print(i)

##input

n=int(input("Enter the number: "))
even_numbers(n)

'''output
Enter the number: 10
2
4
6
8
10
'''
