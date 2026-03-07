# check three digit number is natural number or not
# taking input from user

num = int(input("Enter a three digit number: "))
# check if the number is a three digit number
if num >= 100 and num <= 999:   
    print(num, "is a three digit number.")
else:

    print(num, "is not a three digit number.")

    '''Output:
    Enter a three digit number: 123
    123 is a three digit number.
    Enter a three digit number: 99
    99 is not a three digit number.'''
    
