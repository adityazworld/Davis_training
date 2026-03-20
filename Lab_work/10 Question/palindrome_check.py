## question 8)
def is_palindrome(value):
    value = str(value)
    
    reversed_val = ""
    for i in range(len(value)-1, -1, -1):
        reversed_val += value[i]

    if value == reversed_val:
        print("Palindrome")
    else:
        print("Not Palindrome")


user_input = input("Enter number/string: ")
is_palindrome(user_input)